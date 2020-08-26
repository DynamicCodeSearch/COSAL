package edu.ncsu.config.hyperparameters;


public class HyperParameters {

    public final static float STRING_MUTATION_PROBABILITY = 0.5f;

    /**
     * Minimum statement size to consider
     */
    public final static int MIN_STATEMENT_SIZE = 1;

    /***
     * Maximum number of arguments per function.
     */
    public final static int MAX_NUM_ARGS = 5;

    /**
     * Maximum array size
     */
    public final static int MAX_ARRAY_SIZE = 100;
//    public static int MAX_ARRAY_SIZE = 5;

    /***
     * Number of arguments to generate while fuzzing
     */
    public final static int FUZZ_ARGUMENT_SIZE = 256;
//    public static int FUZZ_ARGUMENT_SIZE = 3;

    public final static int DYNAMIC_VALIDATION_ARGUMENT_SIZE = 32;


    /***
     * Number of arguments to sample from
     */
    public final static int SAMPLE_ARGUMENT_SIZE = FUZZ_ARGUMENT_SIZE * 2;

    public final static int TEST_FUZZ_ARGUMENT_SIZE = FUZZ_ARGUMENT_SIZE * 5;

    /**
     * Maximum wait time for execution in milliseconds
     */
    public final static int METHOD_EXECUTION_WAIT_TIME = 100;

    /**
     * Maximum wait time for all executions
     */
    public final static int ALL_METHOD_EXECUTIONS_WAIT_MULTIPLIER = 2;


    /***
     * Three seconds
     */
    public final static int THREE_SECS = 3 * 1000;


    /***
     * Constructor Expansion while permutation. Can be one of
     * 1) OPTIMAL - The most verbose constructor is chosen
     * 2) ALL - All the constructors are chosen.
     */
    public final static ConstructorExpansion CONSTRUCTOR_EXPANSION = ConstructorExpansion.ALL;


    public final static SnipperMode SNIPPER_MODE = SnipperMode.STATEMENT;

    /***
     * Tokenization
     */
    public final static int TOKEN_SIZE = 5;

    public final static int MIN_CONTEXT_TOKEN_SIZE = 3;


}
