// This package
package config

// Package import
import (
  "encoding/json"
  "errors"
  "fmt"
  "io/ioutil"
)

// To correctly handle imports in Go:
// http://michaelwhatcott.com/gosublime-goimports/

// To get a backtrace, issue ABRT:
// kill -ABRT pid

// Printing and logging.
fmt.Println("Message")
fmt.Printf("%+v", user)
log.Println("Message")

// Loops
for i, site := range sites {
	// i = index, site = value
}
for i := len(dstList) - 1; i >= 0; i-- {

}

// Maps
m = make(map[string]int) // Same as map[string]int{}
m["route"] = 66
i := m["route"]
n := len(m)
delete(m, "route")

// Conversions.
ready := false
readyString := strconv.FormatBool(ready)

strconv.Itoa(43)

strconv.Atoi("65")

if w, ok := weirdType(7).(int); ok {
    i += w
}

// Joining and exploding
s := []string{b.Endpoint, b.Port, b.Host, b.BindingId, strconv.FormatBool(b.Failover), b.State}
joined := strings.Join(s, ":")

message := "We can " + variable + " concat strings"

exploded := strings.Split(joined)

joined := fmt.Sprintf("%s is a joined string", "This")

strings.Split("a man a plan a canal panama", "a ")

arr = append(arr, appendedValue)

// To make a ToString method
func (b bin) String() string {
	return fmt.Sprintf("%b", b)
}

myVar := `This
is a
multi line string`

// Maps
if val, ok := dict["foo"]; ok {

}

// Get the path to the current package.
func packagePath() string {
	_, filename, _, _ := runtime.Caller(0)
	return filepath.Dir(filename)
}

// Getting the type with the reflect package.
typeVar := reflect.TypeOf(variable)

// Switch (no automatic fallthrough, but there is a clause to force it)
switch {
case '0' <= c && c <= '9':
    return c - '0'
case 'a' <= c && c <= 'f':
    return c - 'a' + 10
case 'A' <= c && c <= 'F':
    return c - 'A' + 10
}
return 0

// Return an error
err := errors.New("emit macho dwarf: elf header corrupted")
return fmt.Errorf("Error: %v", err)
