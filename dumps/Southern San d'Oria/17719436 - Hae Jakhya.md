# 17719436 - Hae Jakhya

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 348 bytes                     |
| Total Events     | 13                            |
| References Count | 8                             |

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
| [610](#event-610)        | 0x006C       |     36 |             11 |
| [611](#event-611)        | 0x0090       |     58 |             17 |
| [612](#event-612)        | 0x00CA       |     40 |             13 |
| [65535.8](#event-655358) | 0x00F2       |      3 |              2 |
| [63](#event-63)          | 0x00F5       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x19D3      |        6611 |
|       3 | 0x19D4      |        6612 |
|       4 | 0x19D5      |        6613 |
|       5 | 0x19D6      |        6614 |
|       6 | 0x19D7      |        6615 |
|       7 | 0x19D8      |        6616 |

## String References

- **6611**: Oh... I thought perhaps that somewhere within these walls I would find my prrrince charming...
- **6612**: What's that? Do I know you?
- **6613**: A library book? Ah! That's rrright! That book I borrowed in Windurst.
- **6614**: I totally forgot! How silly of me. Here you are!
- **6615**: That book, $3, was so good! The Library of Magic in Windurst is truly a balm for book lovers...
- **6616**: I know the rrright man for me is out there, somewhere. Oh...

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
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
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 6C 6B 32 00                              ..tlk2.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
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
0040: 74 6C 6B 32 00                                    tlk2.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
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
0040:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=50*
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
0050:                53 F8 FF  FF 7F F8 FF FF 7F 70 61       S........pa
0060: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
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

### Event 610

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 36 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      1E F0 FF FF              ....
0070: 7F 6F 70 29 08 8C 60 0E  01 01 1D 02 80 23 29 08  .op)..`......#).
0080: 8C 60 0E 01 03 29 08 8C  60 0E 01 04 20 00 21 00  .`...)..`... .!.
```

#### Opcodes

```
  0: 0x006C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0072 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0073 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x01)
  4: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=6611*)
    → "Oh... I thought perhaps that somewhere within these walls I would find my prrrince charming..."
  5: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x03)
  7: 0x0085 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x04)
  8: 0x008C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x008E [0x21] END_EVENT
 10: 0x008F [0x00] END_REQSTACK()
```

### Event 611

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 58 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 1E F0 FF FF 7F 6F 70 29  08 8C 60 0E 01 01 1D 03  .....op)..`.....
00A0: 80 23 29 08 8C 60 0E 01  03 29 08 8C 60 0E 01 04  .#)..`...)..`...
00B0: 1D 04 80 23 29 08 8C 60  0E 01 05 1D 05 80 23 29  ...#)..`......#)
00C0: 08 8C 60 0E 01 06 20 00  21 00                    ..`... .!.      
```

#### Opcodes

```
  0: 0x0090 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0095 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0096 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0097 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x01)
  4: 0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=6612*)
    → "What's that? Do I know you?"
  5: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x03)
  7: 0x00A9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x04)
  8: 0x00B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=6613*)
    → "A library book? Ah! That's rrright! That book I borrowed in Windurst."
  9: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00B4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x05)
 11: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=6614*)
    → "I totally forgot! How silly of me. Here you are!"
 12: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00BF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x06)
 14: 0x00C6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 15: 0x00C8 [0x21] END_EVENT
 16: 0x00C9 [0x00] END_REQSTACK()
```

### Event 612

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 40 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                1E F0 FF FF 7F 6F            .....o
00D0: 70 29 08 8C 60 0E 01 01  1D 06 80 23 1D 07 80 23  p)..`......#...#
00E0: 29 08 8C 60 0E 01 03 29  08 8C 60 0E 01 04 20 00  )..`...)..`... .
00F0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00CA [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00D0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x01)
  4: 0x00D8 [0x1D] PRINT_EVENT_MESSAGE(message_id=6615*)
    → "That book, $3, was so good! The Library of Magic in Windurst is truly a balm for book lovers..."
  5: 0x00DB [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=6616*)
    → "I know the rrright man for me is out there, somewhere. Oh..."
  7: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00E0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x03)
  9: 0x00E7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakhya (ID: 17719436/0x010E608C), tag_num=0x04)
 10: 0x00EE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x00F0 [0x21] END_EVENT
 12: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F2  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       22 01 00                                      "..           
```

#### Opcodes

```
  0: 0x00F2 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00F4 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F5  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                22 01 00                                "..        
```

#### Opcodes

```
  0: 0x00F5 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00F7 [0x00] END_REQSTACK()
```
