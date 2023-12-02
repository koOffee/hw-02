#!/bin/bash
include configs/.env.config

.PHONY: lint
lint:
	flake8 src/

prepare:
	apt-get update && apt-get --yes install unzip git g++ libgl1
	mkdir datasets && \
	cd datasets && \
	wget https://clck.ru/36tgHp -O data_segmentation.zip && \
	unzip data_segmentation.zip && \
	rm data_segmentation.zip && \
	cd .. && \
	git clone https://github.com/ultralytics/yolov5 --branch v7.0 && \
	python3 -m venv ./venv && \
	. venv/bin/activate && \
	pip3 install -r requirements/requirements.txt && \
	pip3 install --upgrade --force-reinstall Pillow==9.5.0 && \
	python3 prepare_data.py && \
	cp barcodes.yaml yolov5/data/barcodes.yaml

run:
	cd yolov5 && \
	python train.py --weights $(weights) \
					--cfg $(cfg) \
					--data $(data) \
					--hyp $(hyp) \
					--epochs $(epochs) \
					--batch-size $(batch-size) \
					--imgsz $(imgsz) \
					--device $(device) \
					--optimizer $(optimizer) \
					--project $(project) \
					--name $(name) \
					--cos-lr

.PHONY: install
install:
	pip install -r requirements/requirements.txt

.PHONY: install_dev
install_dev:
	pip install -r requirements/requirements.dev.txt

.PHONY: pre_push_test
pre_push_test: install_dev lint
