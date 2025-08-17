# 17752130 - Pakesse-Myukesse

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 316 bytes                 |
| Total Events     | 12                        |
| References Count | 8                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     22 |              4 |
| [65535.5](#event-655355) | 0x004D       |     16 |              2 |
| [65535.6](#event-655356) | 0x005D       |     22 |              4 |
| [65535.7](#event-655357) | 0x0073       |      9 |              3 |
| [434](#event-434)        | 0x007C       |     29 |             10 |
| [420](#event-420)        | 0x0099       |      1 |              1 |
| [65535.8](#event-655358) | 0x009A       |     45 |             13 |
| [65535.9](#event-655359) | 0x00C7       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0x20A7      |        8359 |
|       3 | 0x2080      |        8320 |
|       4 | 0x2081      |        8321 |
|       5 | 0x2082      |        8322 |
|       6 | 0x2083      |        8323 |
|       7 | 0x2088      |        8328 |

## String References

- **8320**: Hey, leave the explanation of black magic to me!
- **8321**: Black magic is used mainly for attacking. As you can tell from their names, black mages are pros at casting black magic.
- **8322**: Black magic has a strong connection to the elements, the magic power abundant in nature. That's why there are spells called Fire and Thunder, which correspond to the elements of fire and lightning.
- **8323**: Black magic is the best. Whenever you say "magic-user," you immediately think of black mages, right?
- **8328**: Oh yeah? But red mages can only use a little bit of black and white magic. I'd call them "monochrome" at best! They're so limited!
- **8359**: It's not that we in the beginners class can't do magic properly... It's just that those guys in the advanced class are too good at casting them spells.

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
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
0020:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 6C 6B 31 00                              ..tlk1.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=85*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 6C 6B 31 5E 69 64 6C  30 1C 01 80 00           tlk1^idl0....   
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0049 [0x1C] WAIT(30* ticks)
  3: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         5B 00 80               [..
0050: F8 FF FF 7F F8 FF FF 7F  65 68 65 30 00           ........ehe0.   
```

#### Opcodes

```
  0: 0x004D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ehe0" with entities [EventEntity, EventEntity], work=85*
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         53 F8 FF               S..
0060: FF 7F F8 FF FF 7F 65 68  65 30 5E 69 64 6C 30 1C  ......ehe0^idl0.
0070: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x005D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehe0" with entities [EventEntity, EventEntity]
  1: 0x006A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x006F [0x1C] WAIT(30* ticks)
  3: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0073  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          5E 69 64 6C 30  1C 01 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x0073 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0078 [0x1C] WAIT(30* ticks)
  2: 0x007B [0x00] END_REQSTACK()
```

### Event 434

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      1E F0 FF FF              ....
0080: 7F 6F 70 29 08 42 E0 0E  01 01 1D 02 80 23 29 08  .op).B.......#).
0090: 42 E0 0E 01 02 20 00 21  00                       B.... .!.       
```

#### Opcodes

```
  0: 0x007C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0081 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0082 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0083 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x01)
  4: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=8359*)
    → "It's not that we in the beginners class can't do magic properly... It's just that those guys in the advanced class are too good at casting them spells."
  5: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x02)
  7: 0x0095 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0097 [0x21] END_EVENT
  9: 0x0098 [0x00] END_REQSTACK()
```

### Event 420

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0099  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             00                             .      
```

#### Opcodes

```
  0: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 45 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                29 08 42 E0 0E 01            ).B...
00A0: 03 1D 03 80 23 1D 04 80  23 1D 05 80 23 29 08 42  ....#...#...#).B
00B0: E0 0E 01 04 29 08 42 E0  0E 01 05 1D 06 80 23 29  ....).B.......#)
00C0: 08 42 E0 0E 01 06 00                              .B.....         
```

#### Opcodes

```
  0: 0x009A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x03)
  1: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=8320*)
    → "Hey, leave the explanation of black magic to me!"
  2: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=8321*)
    → "Black magic is used mainly for attacking. As you can tell from their names, black mages are pros at casting black magic."
  4: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00A9 [0x1D] PRINT_EVENT_MESSAGE(message_id=8322*)
    → "Black magic has a strong connection to the elements, the magic power abundant in nature. That's why there are spells called Fire and Thunder, which correspond to the elements of fire and lightning."
  6: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00AD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x04)
  8: 0x00B4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x05)
  9: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=8323*)
    → "Black magic is the best. Whenever you say "magic-user," you immediately think of black mages, right?"
 10: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00BF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x06)
 12: 0x00C6 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C7   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      29  08 42 E0 0E 01 01 1D 07         ).B......
00D0: 80 23 29 08 42 E0 0E 01  02 00                    .#).B.....      
```

#### Opcodes

```
  0: 0x00C7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x01)
  1: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=8328*)
    → "Oh yeah? But red mages can only use a little bit of black and white magic. I'd call them "monochrome" at best! They're so limited!"
  2: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Pakesse-Myukesse (ID: 17752130/0x010EE042), tag_num=0x02)
  4: 0x00D9 [0x00] END_REQSTACK()
```
