# 16830665 - Apkallu Interpreter

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Mine Shaft #2716 (ID: 13) |
| Block Size       | 180 bytes                 |
| Total Events     | 10                        |
| References Count | 3                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     14 |              2 |
| [65535.2](#event-655352) | 0x000F       |     14 |              2 |
| [65535.3](#event-655353) | 0x001D       |     14 |              2 |
| [65535.4](#event-655354) | 0x002B       |     14 |              2 |
| [65535.5](#event-655355) | 0x0039       |     13 |              2 |
| [65535.6](#event-655356) | 0x0046       |     13 |              2 |
| [65535.7](#event-655357) | 0x0053       |     13 |              2 |
| [8](#event-8)            | 0x0060       |      7 |              2 |
| [32001](#event-32001)    | 0x0067       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0489      |        1161 |
|       1 | 0x048B      |        1163 |
|       2 | 0x0488      |        1160 |

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
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2C F8 FF FF 7F F8 FF  FF 7F 73 70 30 31 00      ,........sp01. 
```

#### Opcodes

```
  0: 0x0001 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp01" with entities [EventEntity, EventEntity]
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               53                 S
0010: F8 FF FF 7F F8 FF FF 7F  73 70 30 31 00           ........sp01.   
```

#### Opcodes

```
  0: 0x000F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp01" with entities [EventEntity, EventEntity]
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         2C F8 FF               ,..
0020: FF 7F F8 FF FF 7F 73 70  30 32 00                 ......sp02.     
```

#### Opcodes

```
  0: 0x001D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp02" with entities [EventEntity, EventEntity]
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   53 F8 FF FF 7F             S....
0030: F8 FF FF 7F 73 70 30 32  00                       ....sp02.       
```

#### Opcodes

```
  0: 0x002B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp02" with entities [EventEntity, EventEntity]
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             C4 02 00 80 F8 FF FF           .......
0040: 7F F0 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0039 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): EventEntity casts magic 1161* on LocalPlayer
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   C4 02  01 80 F8 FF FF 7F F0 FF        ..........
0050: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0046 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): EventEntity casts magic 1163* on LocalPlayer
  1: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          C4 02 02 80 F8  FF FF 7F F0 FF FF 7F 00     .............
```

#### Opcodes

```
  0: 0x0053 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): EventEntity casts magic 1160* on LocalPlayer
  1: 0x005F [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0060 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0067 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006D [0x00] END_REQSTACK()
```
