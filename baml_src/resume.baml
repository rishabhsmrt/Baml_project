enum Market_Indicator {
    OPEN
    HIGH
    LOW
    PREV_CLOSE
    Percentage_CHNG
    VOLUME_TRADED 
}

// Defining a data model.
class Stock {
  name string[] @description("Represents the name of stock price listed on National Stock Exchange India in Capital Letters")
  market_parameters Market_Indicator[] @description(#"
    Represent the what parameter is required to compare to stocks.
  "#)
}

// Create a function to extract the resume from a string.
function ExtractResume(resume: string) -> Stock {
  // Specify a client as provider/model-name
  // you can use custom LLM params with a custom client name from clients.baml like "client CustomHaiku"
  client "Mistral" // Set OPENAI_API_KEY to use this client.
  prompt #"
    You are helpful agent which will extract the stock names and labels (like stock price and volume traded) from the given paragraph.
    {{ resume }}
    ----
    {{ ctx.output_format }}
    ---
  "#
}



// Test the function with a sample resume. Open the VSCode playground to run this.
test Get_stock_names {
  functions [ExtractResume]
  args {
    resume #"
      What is the high price and low price for TCS and ongc.
    "#
  }
}
