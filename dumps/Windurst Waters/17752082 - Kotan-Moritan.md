# 17752082 - Kotan-Moritan

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 352 bytes                 |
| Total Events     | 13                        |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [377](#event-377)        | 0x0030       |     33 |             12 |
| [166](#event-166)        | 0x0051       |     29 |             10 |
| [174](#event-174)        | 0x006E       |     29 |             10 |
| [391](#event-391)        | 0x008B       |     33 |             12 |
| [407](#event-407)        | 0x00AC       |     33 |             12 |
| [722](#event-722)        | 0x00CD       |     29 |             10 |
| [1156](#event-1156)      | 0x00EA       |      1 |              1 |
| [1157](#event-1157)      | 0x00EB       |      1 |              1 |
| [1159](#event-1159)      | 0x00EC       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0x1FF3      |        8179 |
|       3 | 0x1FF4      |        8180 |
|       4 | 0x1E0A      |        7690 |
|       5 | 0x1E1E      |        7710 |
|       6 | 0x202B      |        8235 |
|       7 | 0x202C      |        8236 |
|       8 | 0x204E      |        8270 |
|       9 | 0x204F      |        8271 |
|      10 | 0x25DA      |        9690 |

## String References

- **7690**: What's going on? The minister seems to be troubled... But the dimwit at the counter is half-asleep as usual.
- **7710**: What's going on? The minister seems to be troubled... But the dimwit at the counter is half-asleep as usual.
- **8179**: I'm going to read as many books as I can. With all that knowledge, I can become valedictorian of the School of Magic!
- **8180**: Then when I graduate, I'll enter one of the ministries, work my way up to minister, then become a professor when I retire.
- **8235**: A Hume named Orn? Why would we know that? If it doesn't appear in our exams, then it's not worth learning!
- **8236**: You should ask adults such trivial questions. They have more time on their handy-wandies.
- **8270**: Did you know...? They say that everyone in this world has at least one other person who looks exactly like them.
- **8271**: So that means there's another Kotan-Moritan who looks exactly like me out there somewhere! Man, that's pretty cool when you think about it.
- **9690**: What's going on? The minister seems to be troubled. But the dimwit at the counter is half asleep as usual.

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

### Event 377

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  08 12 E0 0E 01 01 1D 02  .....op)........
0040: 80 23 1D 03 80 23 29 08  12 E0 0E 01 02 20 00 21  .#...#)...... .!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x01)
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8179*)
    → "I'm going to read as many books as I can. With all that knowledge, I can become valedictorian of the School of Magic!"
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=8180*)
    → "Then when I graduate, I'll enter one of the ministries, work my way up to minister, then become a professor when I retire."
  7: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0046 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x02)
  9: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x004F [0x21] END_EVENT
 11: 0x0050 [0x00] END_REQSTACK()
```

### Event 166

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    1E F0 FF FF 7F 6F 70  29 08 12 E0 0E 01 01 1D   .....op).......
0060: 04 80 23 29 08 12 E0 0E  01 02 20 00 21 00        ..#)...... .!.  
```

#### Opcodes

```
  0: 0x0051 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0057 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0058 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x01)
  4: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7690*)
    → "What's going on? The minister seems to be troubled... But the dimwit at the counter is half-asleep as usual."
  5: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0063 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x02)
  7: 0x006A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x006C [0x21] END_EVENT
  9: 0x006D [0x00] END_REQSTACK()
```

### Event 174

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            1E F0                ..
0070: FF FF 7F 6F 70 29 08 12  E0 0E 01 01 1D 05 80 23  ...op).........#
0080: 29 08 12 E0 0E 01 02 20  00 21 00                 )...... .!.     
```

#### Opcodes

```
  0: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0074 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0075 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x01)
  4: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=7710*)
    → "What's going on? The minister seems to be troubled... But the dimwit at the counter is half-asleep as usual."
  5: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0080 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x02)
  7: 0x0087 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0089 [0x21] END_EVENT
  9: 0x008A [0x00] END_REQSTACK()
```

### Event 391

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   1E F0 FF FF 7F             .....
0090: 6F 70 29 08 12 E0 0E 01  01 1D 06 80 23 1D 07 80  op).........#...
00A0: 23 29 08 12 E0 0E 01 02  20 00 21 00              #)...... .!.    
```

#### Opcodes

```
  0: 0x008B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0090 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0091 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0092 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x01)
  4: 0x0099 [0x1D] PRINT_EVENT_MESSAGE(message_id=8235*)
    → "A Hume named Orn? Why would we know that? If it doesn't appear in our exams, then it's not worth learning!"
  5: 0x009C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x009D [0x1D] PRINT_EVENT_MESSAGE(message_id=8236*)
    → "You should ask adults such trivial questions. They have more time on their handy-wandies."
  7: 0x00A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00A1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x02)
  9: 0x00A8 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00AA [0x21] END_EVENT
 11: 0x00AB [0x00] END_REQSTACK()
```

### Event 407

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      1E F0 FF FF              ....
00B0: 7F 6F 70 29 08 12 E0 0E  01 01 1D 08 80 23 1D 09  .op).........#..
00C0: 80 23 29 08 12 E0 0E 01  02 20 00 21 00           .#)...... .!.   
```

#### Opcodes

```
  0: 0x00AC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x01)
  4: 0x00BA [0x1D] PRINT_EVENT_MESSAGE(message_id=8270*)
    → "Did you know...? They say that everyone in this world has at least one other person who looks exactly like them."
  5: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=8271*)
    → "So that means there's another Kotan-Moritan who looks exactly like me out there somewhere! Man, that's pretty cool when you think about it."
  7: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00C2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x02)
  9: 0x00C9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00CB [0x21] END_EVENT
 11: 0x00CC [0x00] END_REQSTACK()
```

### Event 722

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         1E F0 FF               ...
00D0: FF 7F 6F 70 29 08 12 E0  0E 01 01 1D 0A 80 23 29  ..op).........#)
00E0: 08 12 E0 0E 01 02 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x00CD [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00D2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00D3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x01)
  4: 0x00DB [0x1D] PRINT_EVENT_MESSAGE(message_id=9690*)
    → "What's going on? The minister seems to be troubled. But the dimwit at the counter is half asleep as usual."
  5: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00DF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kotan-Moritan (ID: 17752082/0x010EE012), tag_num=0x02)
  7: 0x00E6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00E8 [0x21] END_EVENT
  9: 0x00E9 [0x00] END_REQSTACK()
```

### Event 1156

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                00                           .     
```

#### Opcodes

```
  0: 0x00EA [0x00] END_REQSTACK()
```

### Event 1157

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   00                         .    
```

#### Opcodes

```
  0: 0x00EB [0x00] END_REQSTACK()
```

### Event 1159

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00EC [0x00] END_REQSTACK()
```
