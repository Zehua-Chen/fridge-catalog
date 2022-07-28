package main

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/go-playground/assert/v2"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func TestCreateUser(t *testing.T) {
	db, _ := gorm.Open(sqlite.Open("file::memory:?cache=shared"), &gorm.Config{})
	entities.Migrate(db)

	router := setupRouter(db)

	postUser := func(user entities.User) entities.User {
		body, _ := json.Marshal(user)
		reader := bytes.NewReader(body)

		request, _ := http.NewRequest("POST", "/api/v1/users", reader)
		request.Header.Add("Content-Type", "application/json")

		response := httptest.NewRecorder()
		router.ServeHTTP(response, request)

		bytes, _ := ioutil.ReadAll(response.Body)

		var responseUser entities.User

		json.Unmarshal(bytes, &responseUser)

		return responseUser
	}

	getUsers := func() []entities.User {
		request, _ := http.NewRequest("GET", "/api/v1/users", nil)
		response := httptest.NewRecorder()
		router.ServeHTTP(response, request)

		bytes, _ := ioutil.ReadAll(response.Body)

		var users []entities.User

		json.Unmarshal(bytes, &users)

		return users
	}

	userA := postUser(entities.User{Name: "Peter Griffin", Email: "peter_griffin@outlook.com"})
	userB := postUser(entities.User{Name: "Brian", Email: "brian@outlook.com"})

	// test users can be created
	assert.Equal(t, userA.Name, "Peter Griffin")
	assert.Equal(t, userA.Email, "peter_griffin@outlook.com")

	assert.Equal(t, userB.Name, "Brian")
	assert.Equal(t, userB.Email, "brian@outlook.com")

	// test users ID are unique
	assert.NotEqual(t, userA.ID, userB.ID)

	// test get users
	users := getUsers()

	assert.Equal(t, 2, len(users))

	// TODO: test error cases
}
