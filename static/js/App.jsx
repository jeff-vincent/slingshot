import React from "react";

import Display from './display'
import Controls from './controls'
import uploadButton from './uploadButton'

export default class App extends React.Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    return (
      <div className="container bg-lt-gry blk-border rounded-corners">
        <Display />
        <Controls />
      </div>
    );
  }
}
