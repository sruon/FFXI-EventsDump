# 17613291 - Albertois

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 156 bytes         |
| Total Events     | 8                 |
| References Count | 2                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [43](#event-43)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     16 |              2 |
| [65535.2](#event-655352) | 0x0018       |     14 |              2 |
| [65535.3](#event-655353) | 0x0026       |     16 |              2 |
| [65535.4](#event-655354) | 0x0036       |     14 |              2 |
| [65535.5](#event-655355) | 0x0044       |     16 |              2 |
| [65535.6](#event-655356) | 0x0054       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00EA      |         234 |
|       1 | 0x00A0      |         160 |

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

### Event 43

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          66 00 80 F8 FF FF 7F F8          f.......
0010: FF FF 7F 65 64 30 31 00                           ...ed01.        
```

#### Opcodes

```
  0: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ed01" with entities [EventEntity, EventEntity], work=234*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          53 F8 FF FF 7F F8 FF FF          S.......
0020: 7F 65 64 30 31 00                                 .ed01.          
```

#### Opcodes

```
  0: 0x0018 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ed01" with entities [EventEntity, EventEntity]
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   66 00  80 F8 FF FF 7F F8 FF FF        f.........
0030: 7F 65 64 30 32 00                                 .ed02.          
```

#### Opcodes

```
  0: 0x0026 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ed02" with entities [EventEntity, EventEntity], work=234*
  1: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   53 F8  FF FF 7F F8 FF FF 7F 65        S........e
0040: 64 30 32 00                                       d02.            
```

#### Opcodes

```
  0: 0x0036 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ed02" with entities [EventEntity, EventEntity]
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             66 01 80 F8  FF FF 7F F8 FF FF 7F 6F      f..........o
0050: 72 7A 30 00                                       rz0.            
```

#### Opcodes

```
  0: 0x0044 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "orz0" with entities [EventEntity, EventEntity], work=160*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             53 F8 FF FF  7F F8 FF FF 7F 6F 72 7A      S........orz
0060: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0054 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "orz0" with entities [EventEntity, EventEntity]
  1: 0x0061 [0x00] END_REQSTACK()
```
