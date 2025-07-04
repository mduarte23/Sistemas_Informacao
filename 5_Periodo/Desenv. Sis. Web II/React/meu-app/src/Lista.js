import React, {Component} from 'react';
export default class App extends Component {
    state = {
        data: [],
    }
    // metodo executado depois que o componente é montado
    componentDidMount() {
        fetch ('https://pokeapi.co/api/v2/pokemon?offset=0&limit=100.json')
        .then((result) => result.json())
        .then((result) => {
            this.setState({
                data: result.results,
            })
        })
    }

    render() {
        const result = this.state.data.map((entry, index) => {
            // return <li key={index}>{entry.name}</li>
            return <option value={index}>{entry.name}</option>
        })

        // return <ul>{result}</ul>
        return <select>{result}</select>

        // Alterar o codigo para mostrar todos os Pokemons em um campo select
    }
}