import operations
import logging

logging.basicConfig(
    filename = "test.log",
    level = logging.DEBUG,
    filemode = "w"
)

if __name__ == "__main__":
    #print("hiya papaya")

    logging.info("Test case 1")

    result = operations.add(2,4)

    if result == 6:
        logging.info("PASS")
    else:
        logging.error("FAIL")

    logging.info("Test case 2")

    result2 = operations.power(4,2)

    if result2 == 16:
        logging.info("PASS")
    else:
        logging.error("FAIL")

'''
    logging.info("Hiya Papaya")
    logging.warning("file not found")
    logging.error("test case fail")
    a = 5
    logging.debug(f"The value of a is {a}")
'''