# 17399842 - Shadow of Darkness

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Altar Room (ID: 152) |
| Block Size       | 288 bytes            |
| Total Events     | 18                   |
| References Count | 5                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     14 |              2 |
| [1](#event-1)              | 0x0097       |      1 |              1 |
| [44](#event-44)            | 0x0098       |      7 |              2 |
| [42](#event-42)            | 0x009F       |      1 |              1 |
| [65535.11](#event-6553511) | 0x00A0       |      5 |              3 |
| [65535.12](#event-6553512) | 0x00A5       |      5 |              3 |
| [65535.13](#event-6553513) | 0x00AA       |      5 |              3 |
| [65535.14](#event-6553514) | 0x00AF       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00F8      |         248 |
|       1 | 0x1BC8      |        7112 |
|       2 | 0x1BC9      |        7113 |
|       3 | 0x1BCB      |        7115 |
|       4 | 0x1BCC      |        7116 |

## String References

- **7112**: You are too late... I have already awakened.
- **7113**: Your rage, cowardice, envy, arrogance, and apathy...from these I will spread the bane that will destroy Vana'diel.
- **7115**: Your kind has awakened me...and this time, you will be destroyed!
- **7116**: You cannot stop me. Vana'diel will be the grave for you and all your kind!

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 72 6B 6D 30   [..........rkm0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rkm0" with entities [EventEntity, EventEntity], work=248*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 72 6B 6D 30 00      S........rkm0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "rkm0" with entities [EventEntity, EventEntity]
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
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 75 6B 6D 30 00     ..........ukm0. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ukm0" with entities [EventEntity, EventEntity], work=248*
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
0030: F8 FF FF 7F F8 FF FF 7F  75 6B 6D 30 00           ........ukm0.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ukm0" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         5B 00 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  75 6B 6D 31 00           ........ukm1.   
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ukm1" with entities [EventEntity, EventEntity], work=248*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 75 6B  6D 31 00                 ......ukm1.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ukm1" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   5B 00 80 F8 FF             [....
0060: FF 7F F8 FF FF 7F 75 74  75 30 00                 ......utu0.     
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "utu0" with entities [EventEntity, EventEntity], work=248*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   53 F8 FF FF 7F             S....
0070: F8 FF FF 7F 75 74 75 30  00                       ....utu0.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "utu0" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             5B 00 80 F8 FF FF 7F           [......
0080: F8 FF FF 7F 75 74 75 31  00                       ....utu1.       
```

#### Opcodes

```
  0: 0x0079 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "utu1" with entities [EventEntity, EventEntity], work=248*
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             53 F8 FF FF 7F F8 FF           S......
0090: FF 7F 75 74 75 31 00                              ..utu1.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "utu1" with entities [EventEntity, EventEntity]
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0097  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      00                                  .        
```

#### Opcodes

```
  0: 0x0097 [0x00] END_REQSTACK()
```

### Event 44

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0098  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          4E 01 22 80 09 01 00             N.".... 
```

#### Opcodes

```
  0: 0x0098 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Shadow of Darkness (ID: 17399842/0x01098022)
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 42

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               00                 .
```

#### Opcodes

```
  0: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A0  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 1D 01 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x00A0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7112*)
    → "You are too late... I have already awakened."
  1: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                1D 02 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7113*)
    → "Your rage, cowardice, envy, arrogance, and apathy...from these I will spread the bane that will destroy Vana'diel."
  1: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AA  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                1D 03 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=7115*)
    → "Your kind has awakened me...and this time, you will be destroyed!"
  1: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AF  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               1D                 .
00B0: 04 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7116*)
    → "You cannot stop me. Vana'diel will be the grave for you and all your kind!"
  1: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00B3 [0x00] END_REQSTACK()
```
