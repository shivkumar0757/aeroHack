import React, { Component } from "react";
import { Text, StyleSheet, View, Button } from "react-native";

export default class SimpleApp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      response: "Click to connnect to server",
    };
  }

  connect = () => {
    // ip address get this by typing ipconfig on cmd
    // and copy IPv4 address

    const URL = "http://192.168.0.102:8000/";
    fetch(URL)
      .then((response) => {
        if (response.status == 200) {
          return response.text();
        } else {
          throw new Error("Something is wrong :(");
        }
      })
      .then((responseText) => {
        this.setState({ response: responseText });
      })
      .catch((error) => {
        console.error(error.message);
      });
  };

  render() {
    return (
      <View>
        <Text style={styles.title}>{this.state.response}</Text>
        <Button title="connect" onPress={this.connect}></Button>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 20,
    margin: 50,
  },
});
