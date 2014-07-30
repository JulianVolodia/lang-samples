// This package
package config

// Package import
import (
  "encoding/json"
  "errors"
  "fmt"
  "io/ioutil"
)

// Printing and logging.
fmt.Println("Message")
fmt.Printf("%+v", user)
log.Println("Message")

// Conversions.
ready := false
readyString := strconv.FormatBool(ready)

strconv.Itoa(43)

if w, ok := weirdType(7).(int); ok {
    i += w
}

// Joining and exploding
s := []string{b.Endpoint, b.Port, b.Host, b.BindingId, strconv.FormatBool(b.Failover), b.State}
joined := strings.Join(s, ":")

exploded := strings.Split(joined)

joined := fmt.Sprintf("%s is a joined string", "This")

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

// Switch
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
