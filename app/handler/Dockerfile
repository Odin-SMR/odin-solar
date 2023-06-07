FROM public.ecr.aws/lambda/python:3.10
COPY . ${LAMBDA_TASK_ROOT}
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
CMD [ "handler_modules.lambda_handler.handler" ] 