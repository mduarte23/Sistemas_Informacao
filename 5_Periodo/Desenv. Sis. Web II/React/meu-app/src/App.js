import Formulario from "./Formulario";
import Lista from './Lista';
import Feriado from './Feriado';


function App(){
  return (
    <div>
      <h1>Formulario</h1>
      <Formulario/>
      <h2>Pokemons</h2>
      <Lista/>
      <h2>Feriados</h2>
      <Feriado/>
    </div>
  )
}

export default App;