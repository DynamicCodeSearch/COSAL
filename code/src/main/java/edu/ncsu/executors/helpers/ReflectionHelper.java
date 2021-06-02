package edu.ncsu.executors.helpers;

import java.lang.reflect.*;
import java.util.*;

public class ReflectionHelper {

    public static String[] getParameterNamesViaReflection(Executable methodOrConstructor) throws ParameterNotFoundException{
        Parameter[] parameters;
        if (methodOrConstructor instanceof Method || methodOrConstructor instanceof Constructor) {
            parameters = methodOrConstructor.getParameters();
        } else {
            throw new RuntimeException(String.format("@COSAL: Object '%s' is neither method or constructor. Check its type!",  methodOrConstructor.toString()));
        }
        if (parameters == null || parameters.length == 0)
            return null;
        List<String> paramNames = new ArrayList<>();
        for (Parameter parameter: parameters) {
            if (!parameter.isNamePresent()) {
                throw new ParameterNotFoundException(String.format("@COSAL: Parameter names are not present for method '%s' from class '%s'. Try loading it form the AST",
                        methodOrConstructor.getName(),
                        methodOrConstructor.getDeclaringClass().getName()));
            }
            paramNames.add(parameter.getName());
        }
        return Arrays.asList(paramNames.toArray()).toArray(new String[0]);
    }


    /***
     * Get dimensions of an object.
     * @param clazz - Instance of class
     * @return - Dimensions of class
     */
    @SuppressWarnings("rawtypes")
    public static int getArrayDimensions(Class clazz) {
        Class retClass = clazz;
        int arrayDims = 0;
        while (retClass.isArray()) {
            retClass = retClass.getComponentType();
            arrayDims++;
        }
        return arrayDims;
    }

    /**
     * Package of the class.
     * @param clazz - Instance of class
     * @return - package name
     */
    @SuppressWarnings("rawtypes")
    public static String getPackage(Class clazz) {
        if (clazz.getPackage() == null)
            return null;
        return clazz.getPackage().getName();
    }

    /***
     * Get base instance of class if an array
     * @param clazz - Instance of class
     * @return - Recursively return base instance of class
     */
    @SuppressWarnings("rawtypes")
    public static Class getBaseClass(Class clazz) {
        Class retClass = clazz;
        while (retClass.isArray())
            retClass = retClass.getComponentType();
        return retClass;
    }

    /***
     * Get map of fields for a class
     * @param clazz - Instance of Class
     * @return - Map of Field reflection objects with key as field name
     */
    @SuppressWarnings("rawtypes")
    public static Map<String, Field> getFields(Class clazz) {
        Map<String, Field> fields = new HashMap<>();
        Class currentClazz = clazz;
        while (currentClazz != null && clazz != Object.class) {
            Field[] thisFields = currentClazz.getDeclaredFields();
            for (Field field : thisFields) {
                if (!field.isSynthetic() && !fields.containsKey(field.getName()))
                    fields.put(field.getName(), field);
            }
            currentClazz = currentClazz.getSuperclass();
        }
        return fields;
    }

    /**
     * Convert an object to an array
     * @param arr - Object
     * @return - Convert to Object array
     */
    public static Object[] toObjectArray(Object arr) {
        if (arr instanceof Object[])
            return (Object[]) arr;
        int arrLength = Array.getLength(arr);
        Object[] objects = new Object[arrLength];
        for (int arrIndex = 0; arrIndex < arrLength; arrIndex++)
            objects[arrIndex] = Array.get(arr, arrIndex);
        return objects;
    }

    /**
     * Return a list of non-private constructors for class
      * @param clazz - Instance of Class
     * @return - List of java.reflect.Constructor
     */
    @SuppressWarnings("rawtypes")
    public static List<Constructor> getConstructors(Class clazz) {
        List<Constructor> validConstructors = new ArrayList<>();
        Constructor[] constructors = clazz.getConstructors();
        for (Constructor constructor: constructors) {
            if (Modifier.isPrivate(constructor.getModifiers()))
                continue;
            validConstructors.add(constructor);
        }
        return validConstructors;
    }

    /**
     * Create an array class
     * @param clazz - Base version of the class
     * @param arrayDimensions - Dimensions of the array
     * @return - Array class
     */
    @SuppressWarnings("rawtypes")
    public static Class makeArrayClass(Class clazz, int arrayDimensions) {
        Class baseClass = clazz;
        while (arrayDimensions > 0) {
            baseClass = Array.newInstance(baseClass, 0).getClass();
            arrayDimensions -= 1;
        }
        return baseClass;
    }

    /**
     * Return a list of enclosing class names
     *
     * For eg.
     * ```
     * static class A {
     *     private class B {
     *         static class C {
     *             public class D {}
     *         }
     *     }
     * }
     * getEnclosingClasses(D.class) = ["A", "B", "C"]
     * getEnclosingClasses(C.class) = ["A", "B"]
     * getEnclosingClasses(B.class) = ["A"]
     * getEnclosingClasses(A.class) = []
     *```
     *
     * @param clazz - Instance of class
     * @return - List of names of enclosing classes starting from the outermost class.
     */
    @SuppressWarnings("rawtypes")
    public static List<String> getEnclosingClasses(Class clazz) {
        List<String> enclosingClassNames = new ArrayList<>();
        Class enclosingClass = clazz.getEnclosingClass();
        while (enclosingClass != null) {
            enclosingClassNames.add(0, enclosingClass.getSimpleName());
            enclosingClass = enclosingClass.getEnclosingClass();
        }
        return enclosingClassNames;
    }

    /***
     * Return a class key for the Class clazz.
     * All methods in SLACC should use only this representation as class identifiers.
     * @param clazz - Instance of Class
     * @return - String representation of the Class
     */
    @SuppressWarnings("rawtypes")
    public static String makeKey(Class clazz) {
        String packageName = getPackage(clazz);
        String className = clazz.getSimpleName();
        List<String> enclosingClasses = getEnclosingClasses(clazz);
        enclosingClasses.add(className);
        if (packageName == null) {
            return String.join("$", enclosingClasses);
        } else {
            return String.format("%s.%s", packageName, String.join("$", enclosingClasses));
        }
    }

}
