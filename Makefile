proto-py:
	python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. config.proto

run: proto-py
	python main.py