#!/usr/bin/env python3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pytest_itemcollected(item):
    try:
        par = item.parent.obj
        node = item.obj
        pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
        suf = node.__doc__.strip() if node.__doc__ else node.__name__
        if pref or suf:
            item._nodeid = ' '.join((pref, suf))
    except AttributeError as e:
        # Log the exception if required
        logger.error(f"AttributeError encountered: {e}")
    except Exception as e:
        # Log any other exceptions
        logger.error(f"An unexpected error occurred: {e}")
