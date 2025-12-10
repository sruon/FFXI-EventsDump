# 17736071 - Chat Manual

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 264 bytes              |
| Total Events     | 2                      |
| References Count | 23                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [6106](#event-6106)   | 0x0001       |    147 |             52 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x4274      |       17012 |
|       1 | 0x4275      |       17013 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x4276      |       17014 |
|       5 | 0x4277      |       17015 |
|       6 | 0x4278      |       17016 |
|       7 | 0x4279      |       17017 |
|       8 | 0x0002      |           2 |
|       9 | 0x427A      |       17018 |
|      10 | 0x427B      |       17019 |
|      11 | 0x427C      |       17020 |
|      12 | 0x427D      |       17021 |
|      13 | 0x427E      |       17022 |
|      14 | 0x0003      |           3 |
|      15 | 0x427F      |       17023 |
|      16 | 0x4280      |       17024 |
|      17 | 0x4281      |       17025 |
|      18 | 0x0004      |           4 |
|      19 | 0x4282      |       17026 |
|      20 | 0x4283      |       17027 |
|      21 | 0x4284      |       17028 |
|      22 | 0x4285      |       17029 |

## String References

- **17012**: A manual describing proper chat manners floats in front of you.
- **17013**: Read up on which topic? [None for now./I don't know what to talk about./How can I get people to like me?/What shouldn't I do?/What happens if we don't mesh?]
- **17014**: Perhaps consider starting with a simple greeting. Something like...
- **17015**: "Hello, everyone. My name's <Player>. Nice to meet you!"
- **17016**: Of course, injecting your own personal flavor may act as a conversation starter and help people to remember you.
- **17017**: No matter which route you choose, make sure to always remain polite. There is no better way to start a friendship off on the right foot.
- **17018**: When speaking with others, it's critical to listen and be mindful of what they say.
- **17019**: Always talking and never listening may come across as rude.
- **17020**: Another important point is to always be mindful of the listener. How would you feel if someone said that to you? Think carefully before sending someone a message.
- **17021**: It also helps to be clear and concise.
- **17022**: Being vague might cause others to get the wrong impression.
- **17023**: Be extremely careful when giving out personal information such as your address or telephone number.
- **17024**: Furthermore, refrain from making disparaging or aggressive remarks.
- **17025**: Once you are close to someone, you may be more comfortable letting your hair down, but it is strongly recommended that you refrain from any actions that may be construed as harassment.
- **17026**: After joining a linkshell, you may find that you have difficulty participating in conversation or that your personality is too different from the other members.
- **17027**: One of your options in such a situation is to inform the linkshell leader and then leave.
- **17028**: Finding a linkshell that is the perfect fit might not always be easy, but there is certainly a group out there that will match your feelings and goals.
- **17029**: Once you find those kinds of friends, hold them fast and value them as much as they value you. There is no better way to enjoy life in Vana'diel.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 6106

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 147 bytes |
| Instructions | 9         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 48 00 80 23 24 01   J........H..#$.
0010: 80 02 80 02 80 25 02 00  10 02 80 00 23 00 21 00  .....%......#.!.
0020: 01 8F 00 02 00 10 03 80  00 3E 00 48 04 80 23 48  .........>.H..#H
0030: 05 80 23 48 06 80 23 48  07 80 23 01 8F 00 02 00  ..#H..#H..#.....
0040: 10 08 80 00 5D 00 48 09  80 23 48 0A 80 23 48 0B  ....].H..#H..#H.
0050: 80 23 48 0C 80 23 48 0D  80 23 01 8F 00 02 00 10  .#H..#H..#......
0060: 0E 80 00 74 00 48 0F 80  23 48 10 80 23 48 11 80  ...t.H..#H..#H..
0070: 23 01 8F 00 02 00 10 12  80 00 8F 00 48 13 80 23  #...........H..#
0080: 48 14 80 23 48 15 80 23  48 16 80 23 01 8F 00 01  H..#H..#H..#....
0090: 0E 00 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x48] [System] [17012*]:
    → "A manual describing proper chat manners floats in front of you."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x24] CREATE_DIALOG(message_id=17013*, default_option=0*, option_flags=0*)
    → "Read up on which topic? [None for now./I don't know what to talk about./How can I get people to like me?/What shouldn't I do?/What happens if we don't mesh?]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0023
  6: 0x001E [0x21] END_EVENT
  7: 0x001F [0x00] END_REQSTACK()

SUBROUTINE_008F:
  8: 0x008F [0x01] GOTO 0x000E
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0020 [0x01] GOTO 0x008F
# Dead code (unreachable instructions):
     0x0092 [0x21] END_EVENT
     0x0093 [0x00] END_REQSTACK()
```
