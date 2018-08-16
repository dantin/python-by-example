
.PHONY: clean

clean:
	@echo "clean *.pyc files... "
	@find . -name "*.pyc" -print0 | xargs -0 rm
	@echo "clean pycache directories..."
	@find . -d -name "__pycache__" -print0 | xargs -0 rm -rf
