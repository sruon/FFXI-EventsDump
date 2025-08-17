# 17723618 - Goblin Merrymaker

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 308 bytes                     |
| Total Events     | 10                            |
| References Count | 13                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4740](#event-4740)   | 0x0001       |      5 |              3 |
| [4741](#event-4741)   | 0x0006       |      5 |              3 |
| [4742](#event-4742)   | 0x000B       |      5 |              3 |
| [4743](#event-4743)   | 0x0010       |      5 |              3 |
| [4744](#event-4744)   | 0x0015       |      5 |              3 |
| [4745](#event-4745)   | 0x001A       |      5 |              3 |
| [4746](#event-4746)   | 0x001F       |      5 |              3 |
| [4747](#event-4747)   | 0x0024       |      5 |              3 |
| [4748](#event-4748)   | 0x0029       |    158 |             66 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x450C      |       17676 |
|       1 | 0x450E      |       17678 |
|       2 | 0x450F      |       17679 |
|       3 | 0x0001      |           1 |
|       4 | 0x0102      |         258 |
|       5 | 0x0002      |           2 |
|       6 | 0x00D8      |         216 |
|       7 | 0x4511      |       17681 |
|       8 | 0x4513      |       17683 |
|       9 | 0x4514      |       17684 |
|      10 | 0x4512      |       17682 |
|      11 | 0x4515      |       17685 |
|      12 | 0x450D      |       17677 |

## String References

- **17676**: This for me? In-doo-bid-ably! Could be gooder, but it not bad.
- **17677**: Waaah! It you! You give yum-yums for me tum-tum. Good [guy/girl]!
- **17678**: Not for us, not for me? I give it back. Now you happy? Happy toy, happy toy, where be me happy toy?t
- **17679**: No no no no no! Go away! Nose holes busy sniff for happy toy!
- **17681**: You have friend, you do? We Gobbies have friend too.
- **17682**: Yum-yums for me? Gobbies remember...till our tummies go rumble-rumble again.
- **17683**: For me!? Why give so nice thing to me!? Me so happy head go boom! So boom! But first, me need give happy toy to you too.
- **17684**: Happy toy? For me? Why you give so good thing to me? But no can take. Me have no happy toy for you.
- **17685**: Blech. What this yucky thing? It make me want upgut food. Take it away.

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

### Event 4740

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 2E 00 21 00                                  ...!.          
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x002E)
  1: 0x0004 [0x21] END_EVENT
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 4741

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   1A 3B  00 21 00                       .;.!.     
```

#### Opcodes

```
  0: 0x0006 [0x1A] CALL_SUBROUTINE(address=0x003B)
  1: 0x0009 [0x21] END_EVENT
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 4742

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1A 48 00 21 00             .H.!.
```

#### Opcodes

```
  0: 0x000B [0x1A] CALL_SUBROUTINE(address=0x0048)
  1: 0x000E [0x21] END_EVENT
  2: 0x000F [0x00] END_REQSTACK()
```

### Event 4743

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1A 7E 00 21 00                                    .~.!.           
```

#### Opcodes

```
  0: 0x0010 [0x1A] CALL_SUBROUTINE(address=0x007E)
  1: 0x0013 [0x21] END_EVENT
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 4744

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                1A 8A 00  21 00                         ...!.      
```

#### Opcodes

```
  0: 0x0015 [0x1A] CALL_SUBROUTINE(address=0x008A)
  1: 0x0018 [0x21] END_EVENT
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 4745

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1A 97 00 21 00               ...!. 
```

#### Opcodes

```
  0: 0x001A [0x1A] CALL_SUBROUTINE(address=0x0097)
  1: 0x001D [0x21] END_EVENT
  2: 0x001E [0x00] END_REQSTACK()
```

### Event 4746

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1A                 .
0020: A3 00 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x001F [0x1A] CALL_SUBROUTINE(address=0x00A3)
  1: 0x0022 [0x21] END_EVENT
  2: 0x0023 [0x00] END_REQSTACK()
```

### Event 4747

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1A AF 00 21  00                           ...!.       
```

#### Opcodes

```
  0: 0x0024 [0x1A] CALL_SUBROUTINE(address=0x00AF)
  1: 0x0027 [0x21] END_EVENT
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 4748

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0029    |
| Data Size    | 158 bytes |
| Instructions | 9         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1A BB 00 21 00 42 1E           ...!.B.
0030: F0 FF FF 7F 6F 70 1D 00  80 23 1B 42 1E F0 FF FF  ....op...#.B....
0040: 7F 6F 70 1D 01 80 23 1B  42 1E F0 FF FF 7F 6F 70  .op...#.B.....op
0050: 1D 02 80 23 02 02 10 03  80 00 6A 00 73 04 80 F8  ...#......j.s...
0060: FF FF 7F F0 FF FF 7F 01  7D 00 02 02 10 05 80 00  ........}.......
0070: 7D 00 73 06 80 F8 FF FF  7F F0 FF FF 7F 1B 1E F0  }.s.............
0080: FF FF 7F 6F 70 1D 07 80  23 1B 42 1E F0 FF FF 7F  ...op...#.B.....
0090: 6F 70 1D 08 80 23 1B 1E  F0 FF FF 7F 6F 70 1D 09  op...#......op..
00A0: 80 23 1B 1E F0 FF FF 7F  6F 70 1D 0A 80 23 1B 1E  .#......op...#..
00B0: F0 FF FF 7F 6F 70 1D 0B  80 23 1B 1E F0 FF FF 7F  ....op...#......
00C0: 6F 70 1D 0C 80 23 1B                              op...#.         
```

#### Opcodes

```
  0: 0x0029 [0x1A] CALL_SUBROUTINE(address=0x00BB)
  1: 0x002C [0x21] END_EVENT
  2: 0x002D [0x00] END_REQSTACK()

SUBROUTINE_00BB:
  3: 0x00BB [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00C0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00C1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=17677*)
    → "Waaah! It you! You give yum-yums for me tum-tum. Good [guy/girl]!"
  7: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00C6 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x002E [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x002F [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0035 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=17676*)
    → "This for me? In-doo-bid-ably! Could be gooder, but it not bad."
     0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x003A [0x1B] RETURN
     0x003B [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x003C [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0042 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=17678*)
    → "Not for us, not for me? I give it back. Now you happy? Happy toy, happy toy, where be me happy toy?t"
     0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0047 [0x1B] RETURN
     0x0048 [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x0049 [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x004E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x004F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=17679*)
    → "No no no no no! Go away! Nose holes busy sniff for happy toy!"
     0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0054 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x006A
     0x005C [0x73] EventEntity casts magic 258* on LocalPlayer
     0x0067 [0x01] GOTO 0x007D
     0x006A [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x007D
     0x0072 [0x73] EventEntity casts magic 216* on LocalPlayer
     0x007D [0x1B] RETURN
     0x007E [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0083 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0084 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=17681*)
    → "You have friend, you do? We Gobbies have friend too."
     0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0089 [0x1B] RETURN
     0x008A [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x008B [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0090 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0091 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=17683*)
    → "For me!? Why give so nice thing to me!? Me so happy head go boom! So boom! But first, me need give happy toy to you too."
     0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0096 [0x1B] RETURN
     0x0097 [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x009C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x009D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=17684*)
    → "Happy toy? For me? Why you give so good thing to me? But no can take. Me have no happy toy for you."
     0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00A2 [0x1B] RETURN
     0x00A3 [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x00A8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x00A9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=17682*)
    → "Yum-yums for me? Gobbies remember...till our tummies go rumble-rumble again."
     0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00AE [0x1B] RETURN
     0x00AF [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x00B4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x00B5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x00B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=17685*)
    → "Blech. What this yucky thing? It make me want upgut food. Take it away."
     0x00B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00BA [0x1B] RETURN
```
