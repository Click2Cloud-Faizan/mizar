#!/bin/bash

set -euo pipefail

function main() {
    t=120
    # Initial setup for all nodes.
    run_job node-init-daemonset.yaml node-init $t
    # Start transitd on all nodes.
    kubectl apply -f transitd-daemonset.yaml
    validate $running transitd-daemonset.yaml transitd $t
    # Load transit xdp program on main interface of all nodes.
    run_job load-transit-xdp-daemonset.yaml load-transit-xdp $t
}

function run_job() {
    running="running"
    done="done"

    kubectl apply -f $1
    validate $running $1 $2 $3
    validate $done $1 $2 $3
    kubectl delete -f $1
}

function validate() {
    PODS=$(kubectl get pods | grep $3 | awk '{print $1}')
    end=$((SECONDS+$4))

    for POD in ${PODS}; do
        echo -n "Waiting for pod:$POD"
        while [[ $SECONDS -lt $end ]]; do
            if [[ $1 == "running" ]]; then
                check_running $POD
            else
                check_done $POD
            fi
        done
        echo
        if [[ $SECONDS -lt $end ]]; then
            echo "Pod:${POD} now $1!"
        else
            echo "ERROR: ${POD} timed out after $4 seconds!"
            kubectl delete -f $2
            exit 1
        fi
    done

    echo
    echo "All $3 pods now $1!"
    echo
}

function check_done() {
    if [[ $(kubectl logs $1 --tail 1) == "done" ]]; then
        break
    else
        sleep 2
        echo -n "."
    fi
}

function check_running() {
    if [[ $(kubectl get pod $1 -o go-template --template "{{.status.phase}}") == "Running" ]]; then
        break
    else
        sleep 2
        echo -n "."
    fi
}

main