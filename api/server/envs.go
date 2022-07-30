package server

import "os"

func getSalt() string {
	salt, set := os.LookupEnv("FRIDGE_CATALOG_SALT")

	if set {
		return salt
	}

	return "test_salt"
}
