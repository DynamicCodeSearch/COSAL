package edu.ncsu.mos;

import edu.ncsu.mos.semantics.MethodExecutors;

import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.log(Level.SEVERE, String.format("Size of arguments is less than 1. Arguments = %s",
                    Arrays.toString(args)));
            return;
        }
        switch (args[0]) {
            case "execute":
                MethodExecutors.main(Arrays.copyOfRange(args, 1, args.length));
                break;
            default:
                LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal argument '%s'", args[0]));
                break;
        }
    }
}
