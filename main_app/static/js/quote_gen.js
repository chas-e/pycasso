const quotes = [
  "“Art is a line around your thoughts.” – Gustav Klimt",
  "“To be an artist is to believe in life.” – Henry Moore",
  "“Art evokes the mystery without which the world would not exist.” – René Magritte",
  "“The true use of art is, first, to cultivate the artist’s own spiritual nature.” – George Inness",
  "“The principles of true art is not to portray, but to evoke.” – Jerzy Kosinski",
  "“Great art picks up where nature ends.” – Marc Chagall",
  "“The richness I achieve comes from nature, the source of my inspiration.” – Claude Monet",
  "“If I could say it in words there would be no reason to paint.” – Edward Hopper",
  "“I never paint dreams or nightmares. I paint my own reality.” – Frida Kahlo",
  "“If the artist has outer and inner eyes for nature, nature rewards him by giving him inspiration.” – Wassily Kandinsky",
  "“It is not so much where my motivation comes from but rather how it manages to survive.” – Louise Bourgeois",
  "“You don’t take a photograph, you make it.” – Ansel Adams",
  "“The works must be conceived with fire in the soul but executed with clinical coolness.” – Joan Miró",
  "“To my mind one does not put oneself in place of the past, one only adds a new link.” – Paul Cézanne",
  "“I shut my eyes in order to see.” – Paul Gauguin",
  "“The main thing is to be moved, to love, to hope, to tremble, to live.” – Auguste Rodin",
  "“Whether you succeed or not is irrelevant, there is no such thing.  Making your unknown known is the important thing.” – Georgia O’Keeffe",
  "“Creativity takes courage.” – Henri Matisse",
  "“Every artist was first an amateur.” – Ralph Waldo Emerson",
  "“Have no fear of perfection, you'll never reach it.” – Salvador Dalí",
  "“We don’t make mistakes, just happy little accidents.” – Bob Ross",
  "“If you hear a voice within you say ‘you cannot paint,' then by all means paint, and that voice will be silenced.” – Vincent van Gogh",
  "“Every child is an artist. The problem is how to remain an artist once we grow up.” – Pablo Picasso",
  "“Don’t think about making art, just get it done. Let everyone else decide if it’s good or bad, whether they love it or hate it.  While they are deciding, make even more art.” – Andy Warhol",
  "“I want to make paintings that look as if they were made by a child.” – Jean-Michel Basquiat",
  "“No great artist ever sees things as they really are. If he did, he would cease to be an artist.” – Oscar Wilde",
  "“Painting is easy when you don’t know how, but very difficult when you do.” – Edgar Degas",
];

function newQuote() {
  var randomQuote = Math.floor(Math.random() * quotes.length);
  document.getElementById("quoteDisplay").innerHTML = quotes[randomQuote];
}
