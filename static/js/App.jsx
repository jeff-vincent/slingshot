import React from "react";

import Display from './display'
import Controls from './controls'

class App extends React.Component {
 constructor(props) {
   super(props);
 }
 
 render() {
   return (
   <div>
     <Display />
     <Controls />
   </div>  
   );
 }
}
export default App
