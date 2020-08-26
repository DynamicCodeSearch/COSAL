package edu.ncsu.store;

import edu.ncsu.config.Settings;

public class BaseStorage {

    private final static String STORAGE = Settings.getProperty("store");

    public static IArgumentStore loadArgumentStore(String dataset, boolean isFPTest) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                if (isFPTest)
                    return edu.ncsu.store.mongo.ExtendedArgumentStore.loadStore(dataset);
                else
                    return edu.ncsu.store.mongo.ArgumentStore.loadStore(dataset);
            case Settings.JSON_STORAGE:
                return edu.ncsu.store.json.ArgumentStore.loadStore(dataset);
            default:
                throw new RuntimeException(String.format("Unknown store: %s", STORAGE));
        }
    }

    public static IFunctionStore loadFunctionStore(String dataset, boolean isFPTest) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                if (isFPTest)
                    return new edu.ncsu.store.mongo.ExtendedFunctionStore(dataset);
                else
                    return new edu.ncsu.store.mongo.FunctionStore(dataset);
            case Settings.JSON_STORAGE:
                return new edu.ncsu.store.json.FunctionStore(dataset);
            default:
                throw new RuntimeException(String.format("Unknown store: %s", STORAGE));
        }
    }

    public static IMetadataStore loadMetadataStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.MetadataStore(dataset);
            case Settings.JSON_STORAGE:
                return new edu.ncsu.store.json.MetadataStore(dataset);
            default:
                throw new RuntimeException(String.format("Unknown store: %s", STORAGE));
        }
    }

    public static IFunctionStore loadTestFunctionStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.ExtendedFunctionStore(dataset);
            default:
                throw new RuntimeException("Test function storage supported only for mongo");
        }
    }

    public static IClusterStore loadClusterStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.ClusterStore(dataset);
            default:
                throw new RuntimeException("Cluster storage supported only for mongo");
        }
    }

    public static ISystemClassStore loadSystemClassStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.SystemClassStore(dataset);
            default:
                throw new RuntimeException("System class storage supported only for mongo");
        }
    }

    public static IJDKStore loadJDKStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.JDKStore(dataset);
            default:
                throw new RuntimeException("JDK storage supported only for mongo");
        }
    }

    public static ICommonStore loadCommonStore() {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.CommonStore();
            default:
                throw new RuntimeException("Common storage supported only for mongo");
        }
    }

    public static ITokenStore loadTokenStore() {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.TokenStore();
            default:
                throw new RuntimeException("Token storage supported only for mongo");
        }
    }

}
