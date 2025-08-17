# 17391842 - Periduque

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Monastic Cavern (ID: 150) |
| Block Size       | 472 bytes                 |
| Total Events     | 19                        |
| References Count | 15                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     44 |              4 |
| [65535.2](#event-655352)   | 0x002D       |     14 |              2 |
| [65535.3](#event-655353)   | 0x003B       |     16 |              2 |
| [65535.4](#event-655354)   | 0x004B       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0059       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0069       |     22 |              4 |
| [65535.7](#event-655357)   | 0x007F       |     16 |              2 |
| [65535.8](#event-655358)   | 0x008F       |     14 |              2 |
| [65535.9](#event-655359)   | 0x009D       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00AD       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00BB       |      3 |              2 |
| [0](#event-0)              | 0x00BE       |     12 |              3 |
| [65535.12](#event-6553512) | 0x00CA       |     14 |              4 |
| [65535.13](#event-6553513) | 0x00D8       |     19 |              5 |
| [65535.14](#event-6553514) | 0x00EB       |      5 |              3 |
| [65535.15](#event-6553515) | 0x00F0       |     19 |              5 |
| [65535.16](#event-6553516) | 0x0103       |     25 |              6 |
| [65535.17](#event-6553517) | 0x011C       |     33 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0015      |          21 |
|       1 | 0x0014      |          20 |
|       2 | 0x001E      |          30 |
|       3 | 0xFFFFFAF4  |  4294966004 |
|       4 | 0x90C5      |       37061 |
|       5 | 0xFFFFF448  |  4294964296 |
|       6 | 0x0345      |         837 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFFFFA3F  |  4294965823 |
|       9 | 0x9046      |       36934 |
|      10 | 0x1C41      |        7233 |
|      11 | 0x1C42      |        7234 |
|      12 | 0x1C46      |        7238 |
|      13 | 0x1C47      |        7239 |
|      14 | 0x1C48      |        7240 |

## String References

- **7233**: Yes, sire.
- **7234**: Francmage, I've summoned you here today to talk about one thing--the Northlands investigation.
- **7238**: We must take control of this situation immediately. Still, we cannot let them walk about the Northlands freely. Who knows what they're plotting under the guise of this "investigation."
- **7239**: Francmage, listen. Go with the investigation party, and keep a close eye on what our foreign "friends" do. They are up to something, it is certain.
- **7240**: I am sure nothing will come of this, but in case they do find something in that wasteland, do not let them take it. Understood?

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
| Data Size    | 44 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30   f..........poi0
0010: 53 F8 FF FF 7F F8 FF FF  7F 70 6F 69 30 66 00 80  S........poi0f..
0020: F8 FF FF 7F F8 FF FF 7F  70 6F 69 31 00           ........poi1.   
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=21*
  1: 0x0010 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  2: 0x001D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=21*
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         53 F8 FF               S..
0030: FF 7F F8 FF FF 7F 70 6F  69 30 00                 ......poi0.     
```

#### Opcodes

```
  0: 0x002D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   66 00 80 F8 FF             f....
0040: FF 7F F8 FF FF 7F 73 6C  30 30 00                 ......sl00.     
```

#### Opcodes

```
  0: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sl00" with entities [EventEntity, EventEntity], work=21*
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   53 F8 FF FF 7F             S....
0050: F8 FF FF 7F 73 6C 30 30  00                       ....sl00.       
```

#### Opcodes

```
  0: 0x004B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [EventEntity, EventEntity]
  1: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             66 01 80 F8 FF FF 7F           f......
0060: F8 FF FF 7F 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x0059 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             53 F8 FF FF 7F F8 FF           S......
0070: FF 7F 74 6C 6B 30 5E 69  64 6C 30 1C 02 80 00     ..tlk0^idl0.... 
```

#### Opcodes

```
  0: 0x0069 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0076 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x007B [0x1C] WAIT(30* ticks)
  3: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               66                 f
0080: 01 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00     ..........thk1. 
```

#### Opcodes

```
  0: 0x007F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               53                 S
0090: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x008F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         66 01 80               f..
00A0: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x009D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         53 F8 FF               S..
00B0: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x00AD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BB  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   22 00 00                   "..  
```

#### Opcodes

```
  0: 0x00BB [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00BD [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            22 00                ".
00C0: 37 03 80 04 80 05 80 06  80 00                    7.........      
```

#### Opcodes

```
  0: 0x00BE [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00C0 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.292*, z=37.061*, y=-3.000*, direction=73.6°*
  2: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                32 07 80 1F 00 08            2.....
00D0: 80 09 80 05 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x00CA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00CD [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.473*, Z=36.934*, Y=-3.000*
  2: 0x00D5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D7 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D8   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          29 08 E2 60 09 01 03 1D          )..`....
00E0: 0A 80 23 29 08 E2 60 09  01 04 00                 ..#)..`....     
```

#### Opcodes

```
  0: 0x00D8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x03)
  1: 0x00DF [0x1D] PRINT_EVENT_MESSAGE(message_id=7233*)
    → "Yes, sire."
  2: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x04)
  4: 0x00EA [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EB  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   1D 0B 80 23 00             ...#.
```

#### Opcodes

```
  0: 0x00EB [0x1D] PRINT_EVENT_MESSAGE(message_id=7234*)
    → "Francmage, I've summoned you here today to talk about one thing--the Northlands investigation."
  1: 0x00EE [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 29 08 E2 60 09 01 05 1D  0C 80 23 29 08 E2 60 09  )..`......#)..`.
0100: 01 06 00                                          ...             
```

#### Opcodes

```
  0: 0x00F0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x05)
  1: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7238*)
    → "We must take control of this situation immediately. Still, we cannot let them walk about the Northlands freely. Who knows what they're plotting under the guise of this "investigation.""
  2: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00FB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x06)
  4: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0103   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          27 08 E2 60 09  01 01 1D 0D 80 23 2A 08     '..`......#*.
0110: E2 60 09 01 29 08 E2 60  09 01 02 00              .`..)..`....    
```

#### Opcodes

```
  0: 0x0103 [0x27] REQ_SET(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x01)
  1: 0x010A [0x1D] PRINT_EVENT_MESSAGE(message_id=7239*)
    → "Francmage, listen. Go with the investigation party, and keep a close eye on what our foreign "friends" do. They are up to something, it is certain."
  2: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x010E [0x2A] GET_REQ_LEVEL(level=8, entity_id=Periduque (ID: 17391842/0x010960E2))
  4: 0x0114 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x02)
  5: 0x011B [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      29 08 E2 60              )..`
0120: 09 01 07 1D 0E 80 23 29  08 E2 60 09 01 08 29 08  ......#)..`...).
0130: E2 60 09 01 09 29 08 E2  60 09 01 0A 00           .`...)..`....   
```

#### Opcodes

```
  0: 0x011C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x07)
  1: 0x0123 [0x1D] PRINT_EVENT_MESSAGE(message_id=7240*)
    → "I am sure nothing will come of this, but in case they do find something in that wasteland, do not let them take it. Understood?"
  2: 0x0126 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0127 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x08)
  4: 0x012E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x09)
  5: 0x0135 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Periduque (ID: 17391842/0x010960E2), tag_num=0x0A)
  6: 0x013C [0x00] END_REQSTACK()
```
