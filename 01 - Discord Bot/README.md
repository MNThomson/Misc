# Jamesy: The Discord Bot

## Installation

Clone this repository into any folder and install the required dependencies:

`pip3 install -r requirements.txt`

## Bot Token

On the first run, a `.env` file will be created in the base directory. Add your discord bot token which was obtained from the Discord Developer portal.
```
BOT_TOKEN=
```

## Running the Bot

It is highly suggested to run the bot on a server instead of a personal computer. Bot outages are detrimental as reaction roles become unavailable. A free AWS tier could easily run this or a Raspberry Pi is another great solution.

## Commands

#### `!help`

Replies with a simple hello message

#### `!binary [Text to be Converted]`

Converts the arguments of the command into binary notation.

#### `!purge [#]`

Deletes the last `#` messages in the current channel. Defaults to 5 if no number is provided.

#### `@someone`

Pings a random person on the server. Mostly for laughs at people who don't like pings.

#### `!google [Search Result to Google]`

Sends a link from [LetMeGoogleThat](http://letmegooglethat.com/) to inform the person that they need to improve their Googling skills. Some people might be offended, use at your own risk

### Reaction Roles

#### `!set_reaction [Role ID] [Message ID] [Emoji ID]`

`[Role ID]` Sets the role to receive when reacted too. `[Message ID]` Sets the ID of the message on which people will react. `[Emoji ID]` Sets the emoji that people will react with to get the role. This data is then saved in `reaction_roles.txt`.