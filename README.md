# openfaas-commercial-platform-emulator
A program that sits on top of an OpenFaaS serverless deployment that allows you to emulate how much its function executions would cost on AWS Lambda, Good Cloud Functions, IBM Cloud Functions and Microsoft Azure Functions.

To adapt to your own setup, change the IP address in expression1 and expression2 in priceCalc.py to the IP address of your OpenFaaS deployment.

Run priceCalc on the same host as OpenFaaS when you wish to see the current bill calculated for the four platforms.
V1 makes the assumption that all functions are configured to 128MB
