SRC_DIR=./
DST_DIR=./HomeStation/message

#protoc -I=$SRC_DIR --python_out=$DST_DIR protocol/protobuf/DataMessage.proto
protoc --python_out=$DST_DIR protocol/protobuf/DataMessage.proto


