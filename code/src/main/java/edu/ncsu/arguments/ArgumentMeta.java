package edu.ncsu.arguments;

import edu.ncsu.config.hyperparameters.HyperParameters;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class ArgumentMeta {

    private List<String> seenStrings;

    public final static Random RANDOM = new Random();

    private static final String STRING = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    public ArgumentMeta() {
        seenStrings = new ArrayList<>();
    }

    public void updateSeenStrings(String string) {
        this.seenStrings.add(string);
    }

    public boolean hasSeenString() {
        return seenStrings.size() > 0;
    }

    public String getRandomSeenString() {
        if (hasSeenString())
            return seenStrings.get(RANDOM.nextInt(seenStrings.size()));
        return null;
    }

    public static Character randCharacter() {
        return (char) ThreadLocalRandom.current().nextInt(0, 256);
    }

    /**
     * @param length - Length of string
     * @return - Random string of a certain length
     */
    private static String randString(int length) {
        StringBuilder sb = new StringBuilder(length);
        for( int i = 0; i < length; i++ )
            sb.append(STRING.charAt(ThreadLocalRandom.current().nextInt(STRING.length())));
        return sb.toString();
    }

    /**
     * @return - Random string
     */
    public static String randString() {
        return randString(ThreadLocalRandom.current().nextInt(1, 20));
    }


    private String randomMutate(String str) {
        StringBuilder sb = new StringBuilder(str);
        for (int i=0; i<str.length(); i++) {
            if (RANDOM.nextFloat() <= HyperParameters.STRING_MUTATION_PROBABILITY)
                sb.setCharAt(i, randCharacter());
        }
        return sb.toString();
    }

    private String subStringMutator() {
        String seenString = getRandomSeenString();
        assert seenString != null;
        if (seenString.length() == 0) {
            seenString = randString();
        }
        int start = RANDOM.nextInt(seenString.length());
        int end = start + RANDOM.nextInt(seenString.length() - start);
        return seenString.substring(start, end);
    }

    private String randomMutator() {
        String seenString = getRandomSeenString();
        assert seenString != null;
        return randomMutate(seenString);
    }

    private String concatMutator() {
        String seenString1 = getRandomSeenString();
        String seenString2 = getRandomSeenString();
        assert seenString1 != null && seenString2 != null;
        if (seenString1.equals(seenString2))
            seenString2 = randomMutate(seenString2);
        if (RANDOM.nextFloat() < 0.5) {
            return seenString1 + seenString2;
        } else {
            return seenString2 + seenString1;
        }
    }

    public String getStringMutation() {
        int numMutators = 3;
        int index = RANDOM.nextInt(numMutators);
        switch (index) {
            case 0:
                return subStringMutator();
            case 1:
                return randomMutator();
            case 2:
                return concatMutator();
            default:
                throw new RuntimeException(String.format("How did it end up here? We had only %d mutators right?", numMutators));
        }
    }

}
