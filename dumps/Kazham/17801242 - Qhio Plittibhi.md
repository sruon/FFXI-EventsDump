# 17801242 - Qhio Plittibhi

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 264 bytes        |
| Total Events     | 9                |
| References Count | 8                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [154](#event-154)        | 0x0030       |     33 |             12 |
| [189](#event-189)        | 0x0051       |     40 |             13 |
| [155](#event-155)        | 0x0079       |     33 |             12 |
| [313](#event-313)        | 0x009A       |     12 |              3 |
| [315](#event-315)        | 0x00A6       |     12 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x27EC      |       10220 |
|       3 | 0x27ED      |       10221 |
|       4 | 0x2888      |       10376 |
|       5 | 0x2889      |       10377 |
|       6 | 0x2806      |       10246 |
|       7 | 0x2807      |       10247 |

## String References

- **10220**: That guy over therrre in the funny lookin' clothes says he's from some place called Sand-oreo.
- **10221**: I wonder if everybody therrre dresses that funny.
- **10246**: That guy over therrre's been smiling ever since you brought him that doll.
- **10247**: It's pretty and all, but it's not as cute as my stuffed opo-opo.
- **10376**: Hey [misterrr/lady]...
- **10377**: Does everrrybody in the mainlands smell as bad as you?

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
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

### Event 154

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  08 1A A0 0F 01 01 1D 02  .....op)........
0040: 80 23 1D 03 80 23 29 08  1A A0 0F 01 02 20 00 21  .#...#)...... .!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Qhio Plittibhi (ID: 17801242/0x010FA01A), tag_num=0x01)
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=10220*)
    → "That guy over therrre in the funny lookin' clothes says he's from some place called Sand-oreo."
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=10221*)
    → "I wonder if everybody therrre dresses that funny."
  7: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0046 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Qhio Plittibhi (ID: 17801242/0x010FA01A), tag_num=0x02)
  9: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x004F [0x21] END_EVENT
 11: 0x0050 [0x00] END_REQSTACK()
```

### Event 189

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 40 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    1E F0 FF FF 7F 6F 70  29 08 F0 FF FF 7F 03 29   .....op)......)
0060: 08 1A A0 0F 01 01 1D 04  80 23 1D 05 80 23 29 08  .........#...#).
0070: 1A A0 0F 01 02 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x0051 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0057 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0058 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x03)
  4: 0x005F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Qhio Plittibhi (ID: 17801242/0x010FA01A), tag_num=0x01)
  5: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=10376*)
    → "Hey [misterrr/lady]..."
  6: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=10377*)
    → "Does everrrybody in the mainlands smell as bad as you?"
  8: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x006E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Qhio Plittibhi (ID: 17801242/0x010FA01A), tag_num=0x02)
 10: 0x0075 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0077 [0x21] END_EVENT
 12: 0x0078 [0x00] END_REQSTACK()
```

### Event 155

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             1E F0 FF FF 7F 6F 70           .....op
0080: 29 08 1A A0 0F 01 01 1D  06 80 23 1D 07 80 23 29  ).........#...#)
0090: 08 1A A0 0F 01 02 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x0079 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0080 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Qhio Plittibhi (ID: 17801242/0x010FA01A), tag_num=0x01)
  4: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=10246*)
    → "That guy over therrre's been smiling ever since you brought him that doll."
  5: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=10247*)
    → "It's pretty and all, but it's not as cute as my stuffed opo-opo."
  7: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x008F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Qhio Plittibhi (ID: 17801242/0x010FA01A), tag_num=0x02)
  9: 0x0096 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0098 [0x21] END_EVENT
 11: 0x0099 [0x00] END_REQSTACK()
```

### Event 313

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                92 01 F8 FF FF 7F            ......
00A0: 80 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x009A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00A0 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x00A5 [0x00] END_REQSTACK()
```

### Event 315

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   92 01  F8 FF FF 7F 80 F8 FF FF        ..........
00B0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x00A6 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00AC [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x00B1 [0x00] END_REQSTACK()
```
