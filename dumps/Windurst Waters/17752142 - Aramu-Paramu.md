# 17752142 - Aramu-Paramu

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 364 bytes                 |
| Total Events     | 11                        |
| References Count | 14                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [605](#event-605)        | 0x0030       |     33 |             12 |
| [606](#event-606)        | 0x0051       |     33 |             12 |
| [607](#event-607)        | 0x0072       |     33 |             12 |
| [608](#event-608)        | 0x0093       |     33 |             12 |
| [683](#event-683)        | 0x00B4       |     33 |             12 |
| [684](#event-684)        | 0x00D5       |     33 |             12 |
| [638](#event-638)        | 0x00F6       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x22B0      |        8880 |
|       3 | 0x22B1      |        8881 |
|       4 | 0x22B2      |        8882 |
|       5 | 0x22B3      |        8883 |
|       6 | 0x22B4      |        8884 |
|       7 | 0x22B5      |        8885 |
|       8 | 0x22B6      |        8886 |
|       9 | 0x22B7      |        8887 |
|      10 | 0x22DA      |        8922 |
|      11 | 0x22DB      |        8923 |
|      12 | 0x22F4      |        8948 |
|      13 | 0x22F5      |        8949 |

## String References

- **8880**: Welcome to the "Evensong" Restaurant...the jolliest way to end the day...
- **8881**: Take your time and enjoy some of our many delicious dishes.
- **8882**: Welcome to the "Morning Star" Restaurant...the perfect place to start your day.
- **8883**: Take a moment to relax and savor the quietude.
- **8884**: Welcome to the "Bridge of Dreams" Restaurant...the place where your culinary desires are fulfilled.
- **8885**: We have many healthy dishes for you to try.
- **8886**: Welcome to the "Cerulean Stairs" Restaurant...the cheapest and tastiest place in all Windurst.
- **8887**: Today we have fresh seafood by the boatload. Why not try our fish for lunch or dinner?
- **8922**: Naturally, I also am most worried about Jatan-Paratan.
- **8923**: That bard who came from Jeuno the other day appears to be an old traveling companion of his. So I assume that when they got caught up on each other's tales, he suddenly got the urge to start wandering again...?
- **8948**: Each and every one of us have their own problems. But such is the spice of life...
- **8949**: Welcome to the restaurant that resounds with its own sound! Welcome to the Timbre Timbers Tavern!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 605

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  08 4E E0 0E 01 01 1D 02  .....op).N......
0040: 80 23 1D 03 80 23 29 08  4E E0 0E 01 02 20 00 21  .#...#).N.... .!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x01)
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8880*)
    → "Welcome to the "Evensong" Restaurant...the jolliest way to end the day..."
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=8881*)
    → "Take your time and enjoy some of our many delicious dishes."
  7: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0046 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x02)
  9: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x004F [0x21] END_EVENT
 11: 0x0050 [0x00] END_REQSTACK()
```

### Event 606

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    1E F0 FF FF 7F 6F 70  29 08 4E E0 0E 01 01 1D   .....op).N.....
0060: 04 80 23 1D 05 80 23 29  08 4E E0 0E 01 02 20 00  ..#...#).N.... .
0070: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0051 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0057 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0058 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x01)
  4: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=8882*)
    → "Welcome to the "Morning Star" Restaurant...the perfect place to start your day."
  5: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=8883*)
    → "Take a moment to relax and savor the quietude."
  7: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0067 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x02)
  9: 0x006E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0070 [0x21] END_EVENT
 11: 0x0071 [0x00] END_REQSTACK()
```

### Event 607

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       1E F0 FF FF 7F 6F  70 29 08 4E E0 0E 01 01    .....op).N....
0080: 1D 06 80 23 1D 07 80 23  29 08 4E E0 0E 01 02 20  ...#...#).N.... 
0090: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0072 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0077 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0078 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0079 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x01)
  4: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=8884*)
    → "Welcome to the "Bridge of Dreams" Restaurant...the place where your culinary desires are fulfilled."
  5: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=8885*)
    → "We have many healthy dishes for you to try."
  7: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0088 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x02)
  9: 0x008F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0091 [0x21] END_EVENT
 11: 0x0092 [0x00] END_REQSTACK()
```

### Event 608

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          1E F0 FF FF 7F  6F 70 29 08 4E E0 0E 01     .....op).N...
00A0: 01 1D 08 80 23 1D 09 80  23 29 08 4E E0 0E 01 02  ....#...#).N....
00B0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0093 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0098 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0099 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x009A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x01)
  4: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=8886*)
    → "Welcome to the "Cerulean Stairs" Restaurant...the cheapest and tastiest place in all Windurst."
  5: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=8887*)
    → "Today we have fresh seafood by the boatload. Why not try our fish for lunch or dinner?"
  7: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x02)
  9: 0x00B0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00B2 [0x21] END_EVENT
 11: 0x00B3 [0x00] END_REQSTACK()
```

### Event 683

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             1E F0 FF FF  7F 6F 70 29 08 4E E0 0E      .....op).N..
00C0: 01 01 1D 0A 80 23 1D 0B  80 23 29 08 4E E0 0E 01  .....#...#).N...
00D0: 02 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x00B4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00BB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x01)
  4: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=8922*)
    → "Naturally, I also am most worried about Jatan-Paratan."
  5: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=8923*)
    → "That bard who came from Jeuno the other day appears to be an old traveling companion of his. So I assume that when they got caught up on each other's tales, he suddenly got the urge to start wandering again...?"
  7: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00CA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x02)
  9: 0x00D1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00D3 [0x21] END_EVENT
 11: 0x00D4 [0x00] END_REQSTACK()
```

### Event 684

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                1E F0 FF  FF 7F 6F 70 29 08 4E E0       .....op).N.
00E0: 0E 01 01 1D 0C 80 23 1D  0D 80 23 29 08 4E E0 0E  ......#...#).N..
00F0: 01 02 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x00D5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00DA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00DB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00DC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x01)
  4: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8948*)
    → "Each and every one of us have their own problems. But such is the spice of life..."
  5: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8949*)
    → "Welcome to the restaurant that resounds with its own sound! Welcome to the Timbre Timbers Tavern!"
  7: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00EB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Aramu-Paramu (ID: 17752142/0x010EE04E), tag_num=0x02)
  9: 0x00F2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00F4 [0x21] END_EVENT
 11: 0x00F5 [0x00] END_REQSTACK()
```

### Event 638

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00F6 [0x00] END_REQSTACK()
```
