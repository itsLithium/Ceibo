from SPI import build
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

# Add functions
# Add typechecking
# Add const and type declarations

def main():
    
    program = '''
    Program Test;
VAR
a, b, c : INTEGER;

BEGIN {Test}
    BEGIN
        a := 5;  // Assigning values to the variables
        b := 10;
        c := 15;
        writeln("Value of a: ", a );
        writeln("Value of b: ", b );
        writeln("Value of c: ", c );
    END;
END. {Test}
    '''
    build(program)
    # path = "program.txt"
    # if os.path.isfile(path):
    #     with open(path) as f:
    #         program = f.read()
    #         build(program)

if __name__ == '__main__':
    main()

