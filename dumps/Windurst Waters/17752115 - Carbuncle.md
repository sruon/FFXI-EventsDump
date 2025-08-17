# 17752115 - Carbuncle

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 148 bytes                 |
| Total Events     | 7                         |
| References Count | 6                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [846](#event-846)        | 0x001F       |     16 |              3 |
| [65535.3](#event-655353) | 0x002F       |     14 |              4 |
| [850](#event-850)        | 0x003D       |     16 |              3 |
| [920](#event-920)        | 0x004D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0198      |         408 |
|       1 | 0x36B0      |       14000 |
|       2 | 0xFFFD01F5  |  4294771189 |
|       3 | 0xFFFFD9EA  |  4294957546 |
|       4 | 0x042E      |        1070 |
|       5 | 0xFFFFCE32  |  4294954546 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 70 30   [..........pop0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pop0" with entities [EventEntity, EventEntity], work=408*
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
0010:    53 F8 FF FF 7F F8 FF  FF 7F 70 6F 70 30 00      S........pop0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pop0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 846

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               92                 .
0020: 01 F8 FF FF 7F 37 01 80  02 80 03 80 04 80 00     .....7......... 
```

#### Opcodes

```
  0: 0x001F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0025 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.000*, z=-196.107*, y=-9.750*, direction=94.0°*
  2: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               33                 3
0030: 01 37 01 80 02 80 05 80  04 80 33 01 00           .7........3..   
```

#### Opcodes

```
  0: 0x002F [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0031 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.000*, z=-196.107*, y=-12.750*, direction=94.0°*
  2: 0x003A [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  3: 0x003C [0x00] END_REQSTACK()
```

### Event 850

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         92 01 F8               ...
0040: FF FF 7F 37 01 80 02 80  03 80 04 80 00           ...7.........   
```

#### Opcodes

```
  0: 0x003D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0043 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.000*, z=-196.107*, y=-9.750*, direction=94.0°*
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 920

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         00                     .  
```

#### Opcodes

```
  0: 0x004D [0x00] END_REQSTACK()
```
