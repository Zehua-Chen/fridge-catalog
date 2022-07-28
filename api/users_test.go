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
	requestUser := entities.User{Name: "Peter Griffin", Email: "zehua-chen@outlook.com"}

	body, _ := json.Marshal(requestUser)
	reader := bytes.NewReader(body)

	request, _ := http.NewRequest("POST", "/api/v1/users", reader)
	request.Header.Add("Content-Type", "application/json")

	response := httptest.NewRecorder()
	router.ServeHTTP(response, request)

	bytes, _ := ioutil.ReadAll(response.Body)

	var responseUser entities.User

	json.Unmarshal(bytes, &responseUser)

	assert.Equal(t, requestUser.Email, responseUser.Email)
	assert.Equal(t, requestUser.Name, responseUser.Name)
}

func TestGetUsers2(t *testing.T) {
	// t.Fail()
}
