package server_test

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/Zehua-Chen/fridge-catalog/api/server"
	"github.com/go-playground/assert/v2"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func TestCreateUser(t *testing.T) {
	db, _ := gorm.Open(sqlite.Open("file::memory:?cache=shared"), &gorm.Config{})
	entities.Migrate(db)

	router := server.SetupRouter(db)

	postUser := func(user server.PostUserRequest) (server.PostUserResponse, *http.Response) {
		body, _ := json.Marshal(user)
		reader := bytes.NewReader(body)

		request, _ := http.NewRequest("POST", "/api/v1/users", reader)
		request.Header.Add("Content-Type", "application/json")

		response := httptest.NewRecorder()
		router.ServeHTTP(response, request)

		bytes, _ := ioutil.ReadAll(response.Body)

		var responseUser server.PostUserResponse

		json.Unmarshal(bytes, &responseUser)

		return responseUser, response.Result()
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

	userA, responseA := postUser(server.PostUserRequest{
		Name: "Peter Griffin", Email: "peter_griffin@outlook.com", Password: "abc"})

	userB, responseB := postUser(server.PostUserRequest{
		Name: "Brian", Email: "brian@outlook.com", Password: "def"})

	// test users can be created
	assert.Equal(t, userA.Name, "Peter Griffin")
	assert.Equal(t, userA.Email, "peter_griffin@outlook.com")
	assert.Equal(t, responseA.StatusCode, http.StatusCreated)

	assert.Equal(t, userB.Name, "Brian")
	assert.Equal(t, userB.Email, "brian@outlook.com")
	assert.Equal(t, responseB.StatusCode, http.StatusCreated)

	// test users ID are unique
	assert.NotEqual(t, userA.ID, userB.ID)

	// test get users
	users := getUsers()

	assert.Equal(t, 2, len(users))

	// test duplicated email

	userB, response := postUser(server.PostUserRequest{
		Name: "Meg", Email: "brian@outlook.com", Password: "def"})

	assert.Equal(t, response.StatusCode, http.StatusBadRequest)
}
