
.PHONY: clean

clean:
	@echo "clean *.pyc files... "
	@find . -name "*.pyc" -delete
	@echo "clean pycache directories..."
	@find . -name "__pycache__" -delete
