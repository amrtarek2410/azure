#!/bin/bash

SONAR_HOST_URL="http://3.16.139.210:9000"
PROJECT_KEY="amr-test"
SONAR_TOKEN="sqp_a2967e11fd2274239b965d007d70e2c399422fb9"

QG_STATUS=$(curl -s -u $SONAR_TOKEN: $SONAR_HOST_URL/api/qualitygates/project_status?projectKey=$PROJECT_KEY | jq -r '.projectStatus.status')

if [ "$QG_STATUS" = "OK" ]; then
  echo "Quality gate passed"
else
  echo "Quality gate failed"
  exit 1
fi
