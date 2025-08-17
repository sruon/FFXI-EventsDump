# 17752189 - Khuta Colaara

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 272 bytes                 |
| Total Events     | 10                        |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              2 |
| [65535.5](#event-655355) | 0x0045       |     16 |              2 |
| [65535.6](#event-655356) | 0x0055       |     14 |              2 |
| [65535.7](#event-655357) | 0x0063       |      9 |              3 |
| [587](#event-587)        | 0x006C       |     47 |             14 |
| [603](#event-603)        | 0x009B       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0167      |         359 |
|       1 | 0x001E      |          30 |
|       2 | 0x0165      |         357 |
|       3 | 0x228D      |        8845 |
|       4 | 0x228E      |        8846 |
|       5 | 0x22AC      |        8876 |
|       6 | 0x22AD      |        8877 |

## String References

- **8845**: Grrr... I don't have enough gil to buy anything worrrthwhile. Guess I've got to head back out to Sarrrutabarrruta and hunt some more rarrrabs.
- **8846**: Doesn't seem like therrre's any good offerrrs for half-baked adventurrrerrrs like you and me. Betterrr off sticking to rabbiting forrr the time being.
- **8876**: Oh, wow! When did you rrreceive official rrrecognition as an adventurrrerrr?
- **8877**: Why, only the otherrr day you werrre a novice adventurrrerrr like me. Imprrressive!

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  02 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=357*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5B 02 80  F8 FF FF 7F F8 FF FF 7F       [..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=357*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0060: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          5E 69 64 6C 30  1C 01 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x0063 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0068 [0x1C] WAIT(30* ticks)
  2: 0x006B [0x00] END_REQSTACK()
```

### Event 587

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      1E F0 FF FF              ....
0070: 7F 6F 70 29 08 7D E0 0E  01 03 1D 03 80 23 29 08  .op).}.......#).
0080: 7D E0 0E 01 04 29 08 7D  E0 0E 01 05 1D 04 80 23  }....).}.......#
0090: 29 08 7D E0 0E 01 06 20  00 21 00                 ).}.... .!.     
```

#### Opcodes

```
  0: 0x006C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0072 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0073 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khuta Colaara (ID: 17752189/0x010EE07D), tag_num=0x03)
  4: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=8845*)
    → "Grrr... I don't have enough gil to buy anything worrrthwhile. Guess I've got to head back out to Sarrrutabarrruta and hunt some more rarrrabs."
  5: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khuta Colaara (ID: 17752189/0x010EE07D), tag_num=0x04)
  7: 0x0085 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khuta Colaara (ID: 17752189/0x010EE07D), tag_num=0x05)
  8: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=8846*)
    → "Doesn't seem like therrre's any good offerrrs for half-baked adventurrrerrrs like you and me. Betterrr off sticking to rabbiting forrr the time being."
  9: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0090 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khuta Colaara (ID: 17752189/0x010EE07D), tag_num=0x06)
 11: 0x0097 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0099 [0x21] END_EVENT
 13: 0x009A [0x00] END_REQSTACK()
```

### Event 603

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   1E F0 FF FF 7F             .....
00A0: 6F 70 29 08 7D E0 0E 01  01 1D 05 80 23 1D 06 80  op).}.......#...
00B0: 23 29 08 7D E0 0E 01 02  20 00 21 00              #).}.... .!.    
```

#### Opcodes

```
  0: 0x009B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00A2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khuta Colaara (ID: 17752189/0x010EE07D), tag_num=0x01)
  4: 0x00A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=8876*)
    → "Oh, wow! When did you rrreceive official rrrecognition as an adventurrrerrr?"
  5: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=8877*)
    → "Why, only the otherrr day you werrre a novice adventurrrerrr like me. Imprrressive!"
  7: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00B1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Khuta Colaara (ID: 17752189/0x010EE07D), tag_num=0x02)
  9: 0x00B8 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00BA [0x21] END_EVENT
 11: 0x00BB [0x00] END_REQSTACK()
```
