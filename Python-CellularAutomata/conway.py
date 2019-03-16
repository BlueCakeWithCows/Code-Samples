import grid
import sys
import time

def default(str):
    return str + ' [Default: %default]'
    
def readCommand( argv ):
    """
    Processes the command used to run conway from the command line.
    """
    from optparse import OptionParser
    usageStr = """
    USAGE:      python conway.py <options>
    EXAMPLES:   (1) python pacman.py
                    - starts an interactive game
                (2) python pacman.py --layout smallClassic --zoom 2
                OR  python pacman.py -l smallClassic -z 2
                    - starts an interactive game on a smaller board, zoomed in
    """
    parser = OptionParser(usageStr)

    parser.add_option('-n', '--numIterations', dest='numIterations', type='int',
                      help=default('the number of ITERATIONS to run'), metavar='ITERATIONS', default=1)
    parser.add_option('-f', '--inputFile', dest='inputFile',
                      help=default('the Input File from which to load the simulation'),
                      metavar='INPUT_FILE', default='demo.json')
    parser.add_option('-o', '--outputFile', dest='outputFile',
                      help='the Output File to which to store the simulation', default="out.json")
    parser.add_option('--frameTime', dest='frameTime', type='float',
                      help=default('Time to delay between frames; <0 means keyboard'), default=0.1)
    parser.add_option('-r', '--randomize', action='store_true', dest='randomize',
                      help='Display output as text only', default=False)
    parser.add_option('--randomDensity', dest='randomDensity', type='float',
                      help=default('Density of random initial configuration, assuming binary layout'), default=0.4)           
    
          

    options, otherjunk = parser.parse_args(argv)
    if len(otherjunk) != 0:
        raise Exception('Command line input not understood: ' + str(otherjunk))
    args = dict()
    args["num_iterations"] = options.numIterations
    args["input_file"] = options.inputFile
    args["output_file"] = options.outputFile
    args["frame_time"] = options.frameTime
    args["conway_game"] = grid.load(args["input_file"])
    
    if options.randomize:
        import random
        tiles =  args["conway_game"].tiles
        p = options.randomDensity
        for i in range(len(tiles)):
            tiles [i] = 1 if random.random() < p else 0
    
    return args

def runSimulation(conway_game, num_iterations, frame_time, input_file, output_file):
    
    print("Initial State ")
    print(conway_game)
    last_time =  time.time() 
    current_time = time.time()
    for step_number in range(1, num_iterations+1):
        conway_game.update()
        print("Step " + str(step_number))
        print(conway_game)
        current_time = time.time()
        last_time = current_time
        sleep_time = frame_time - (current_time - last_time)
        if sleep_time > 0: time.sleep(sleep_time)
    
    if(output_file is not None):
        grid.save(conway_game, output_file)
        
    return conway_game
    
    
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: conway.py \n See: python pacman.py --help ")
    args = readCommand(sys.argv[1:])
    runSimulation(**args)