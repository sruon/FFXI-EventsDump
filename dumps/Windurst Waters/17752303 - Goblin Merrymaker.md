# 17752303 - Goblin Merrymaker

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 308 bytes                 |
| Total Events     | 10                        |
| References Count | 13                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4720](#event-4720)   | 0x0001       |      5 |              3 |
| [4721](#event-4721)   | 0x0006       |      5 |              3 |
| [4722](#event-4722)   | 0x000B       |      5 |              3 |
| [4723](#event-4723)   | 0x0010       |      5 |              3 |
| [4724](#event-4724)   | 0x0015       |      5 |              3 |
| [4725](#event-4725)   | 0x001A       |      5 |              3 |
| [4726](#event-4726)   | 0x001F       |      5 |              3 |
| [4727](#event-4727)   | 0x0024       |      5 |              3 |
| [4728](#event-4728)   | 0x0029       |    158 |             66 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3D2D      |       15661 |
|       1 | 0x3D2F      |       15663 |
|       2 | 0x3D30      |       15664 |
|       3 | 0x0001      |           1 |
|       4 | 0x0102      |         258 |
|       5 | 0x0002      |           2 |
|       6 | 0x00D8      |         216 |
|       7 | 0x3D32      |       15666 |
|       8 | 0x3D34      |       15668 |
|       9 | 0x3D35      |       15669 |
|      10 | 0x3D33      |       15667 |
|      11 | 0x3D36      |       15670 |
|      12 | 0x3D2E      |       15662 |

## String References

- **15661**: This for me? In-doo-bid-ably! Could be gooder, but it not bad.
- **15662**: Waaah! It you! You give yum-yums for me tum-tum. Good [guy/girl]!
- **15663**: Not for us, not for me? I give it back. Now you happy? Happy toy, happy toy, where be me happy toy?t
- **15664**: No no no no no! Go away! Nose holes busy sniff for happy toy!
- **15666**: You have friend, you do? We Gobbies have friend too.
- **15667**: Yum-yums for me? Gobbies remember...till our tummies go rumble-rumble again.
- **15668**: For me!? Why give so nice thing to me!? Me so happy head go boom! So boom! But first, me need give happy toy to you too.
- **15669**: Happy toy? For me? Why you give so good thing to me? But no can take. Me have no happy toy for you.
- **15670**: Blech. What this yucky thing? It make me want upgut food. Take it away.

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

### Event 4720

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

### Event 4721

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

### Event 4722

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

### Event 4723

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

### Event 4724

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

### Event 4725

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

### Event 4726

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

### Event 4727

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

### Event 4728

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
  6: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=15662*)
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
     0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=15661*)
    → "This for me? In-doo-bid-ably! Could be gooder, but it not bad."
     0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x003A [0x1B] RETURN
     0x003B [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x003C [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0042 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=15663*)
    → "Not for us, not for me? I give it back. Now you happy? Happy toy, happy toy, where be me happy toy?t"
     0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0047 [0x1B] RETURN
     0x0048 [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x0049 [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x004E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x004F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=15664*)
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
     0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=15666*)
    → "You have friend, you do? We Gobbies have friend too."
     0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0089 [0x1B] RETURN
     0x008A [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x008B [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0090 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0091 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=15668*)
    → "For me!? Why give so nice thing to me!? Me so happy head go boom! So boom! But first, me need give happy toy to you too."
     0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0096 [0x1B] RETURN
     0x0097 [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x009C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x009D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=15669*)
    → "Happy toy? For me? Why you give so good thing to me? But no can take. Me have no happy toy for you."
     0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00A2 [0x1B] RETURN
     0x00A3 [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x00A8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x00A9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=15667*)
    → "Yum-yums for me? Gobbies remember...till our tummies go rumble-rumble again."
     0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00AE [0x1B] RETURN
     0x00AF [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x00B4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x00B5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x00B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=15670*)
    → "Blech. What this yucky thing? It make me want upgut food. Take it away."
     0x00B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00BA [0x1B] RETURN
```
