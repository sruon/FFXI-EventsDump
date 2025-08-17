# 17396215 - Daa Bola the Seer

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Castle Oztroja (ID: 151) |
| Block Size       | 276 bytes                |
| Total Events     | 7                        |
| References Count | 8                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [65535.3](#event-655353) | 0x001F       |     16 |              2 |
| [65535.4](#event-655354) | 0x002F       |     14 |              2 |
| [86](#event-86)          | 0x003D       |     50 |             12 |
| [87](#event-87)          | 0x006F       |     88 |             25 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FE      |         254 |
|       1 | 0x1F4D      |        8013 |
|       2 | 0x1F4E      |        8014 |
|       3 | 0x1F4F      |        8015 |
|       4 | 0x1F50      |        8016 |
|       5 | 0x1F51      |        8017 |
|       6 | 0x1F52      |        8018 |
|       7 | 0x1F53      |        8019 |

## String References

- **8013**: Kyah? You being the underling of Zeelozok?
- **8014**: Ka-kyah! Why would Moblins be keeping smoothskins as pets, hoot!?
- **8015**: Ka-kyah!? You being Zeelozok's messenger, here to deliver $1 for Ruu Cogo the Larktongue?
- **8016**: Ka-kyah! Ruu Cogo the Larktongue being done here! Ruu Cogo the Larktongue being no more!
- **8017**: Ka-kyah! Smoothskin being done here, also! Smoothskin be dying soon, too!
- **8018**: Hoot! But I be tiring of war and blood!
- **8019**: This time I be letting you go. Be flying home, smoothskin! Ka-kyah!

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=254*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=254*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 86

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 50 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         79 00 F7               y..
0040: 71 09 01 F0 FF FF 7F 29  08 F7 71 09 01 01 1D 01  q......)..q.....
0050: 80 23 1D 02 80 23 29 08  F7 71 09 01 02 29 08 F7  .#...#)..q...)..
0060: 71 09 01 03 29 08 F7 71  09 01 04 20 00 21 00     q...)..q... .!. 
```

#### Opcodes

```
  0: 0x003D [0x79] Daa Bola the Seer (ID: 17396215/0x010971F7) looks at LocalPlayer (Basic look)
  1: 0x0047 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x01)
  2: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=8013*)
    → "Kyah? You being the underling of Zeelozok?"
  3: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=8014*)
    → "Ka-kyah! Why would Moblins be keeping smoothskins as pets, hoot!?"
  5: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0056 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x02)
  7: 0x005D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x03)
  8: 0x0064 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x04)
  9: 0x006B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x006D [0x21] END_EVENT
 11: 0x006E [0x00] END_REQSTACK()
```

### Event 87

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 88 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               42                 B
0070: 1E F0 FF FF 7F 6F 70 29  08 F7 71 09 01 01 1D 03  .....op)..q.....
0080: 80 23 1D 04 80 23 29 08  F7 71 09 01 02 29 08 F7  .#...#)..q...)..
0090: 71 09 01 03 1D 05 80 23  29 08 F7 71 09 01 04 29  q......#)..q...)
00A0: 08 F7 71 09 01 01 1D 06  80 23 1D 07 80 23 29 08  ..q......#...#).
00B0: F7 71 09 01 02 29 08 F7  71 09 01 03 29 08 F7 71  .q...)..q...)..q
00C0: 09 01 04 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x006F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0070 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0075 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0076 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0077 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x01)
  5: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=8015*)
    → "Ka-kyah!? You being Zeelozok's messenger, here to deliver $1 for Ruu Cogo the Larktongue?"
  6: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0082 [0x1D] PRINT_EVENT_MESSAGE(message_id=8016*)
    → "Ka-kyah! Ruu Cogo the Larktongue being done here! Ruu Cogo the Larktongue being no more!"
  8: 0x0085 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0086 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x02)
 10: 0x008D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x03)
 11: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=8017*)
    → "Ka-kyah! Smoothskin being done here, also! Smoothskin be dying soon, too!"
 12: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0098 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x04)
 14: 0x009F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x01)
 15: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=8018*)
    → "Hoot! But I be tiring of war and blood!"
 16: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=8019*)
    → "This time I be letting you go. Be flying home, smoothskin! Ka-kyah!"
 18: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00AE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x02)
 20: 0x00B5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x03)
 21: 0x00BC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Daa Bola the Seer (ID: 17396215/0x010971F7), tag_num=0x04)
 22: 0x00C3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x00C5 [0x21] END_EVENT
 24: 0x00C6 [0x00] END_REQSTACK()
```
