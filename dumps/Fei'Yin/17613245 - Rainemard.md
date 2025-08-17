# 17613245 - Rainemard

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 116 bytes         |
| Total Events     | 3                 |
| References Count | 4                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [17](#event-17)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     58 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFBF0E  |  4294950670 |
|       1 | 0x10A5F     |       68191 |
|       2 | 0xFFFFC086  |  4294951046 |
|       3 | 0x020A      |         522 |

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

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-16.626*, z=68.191*, y=-16.250*, direction=45.9°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 58 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   80 F8 FF FF 7F             .....
0010: 2C F8 FF FF 7F F8 FF FF  7F 72 65 73 31 53 F8 FF  ,........res1S..
0020: FF 7F F8 FF FF 7F 72 65  73 31 2C F8 FF FF 7F F8  ......res1,.....
0030: FF FF 7F 72 65 73 31 53  F8 FF FF 7F F8 FF FF 7F  ...res1S........
0040: 72 65 73 31 00                                    res1.           
```

#### Opcodes

```
  0: 0x000B [0x80] LOAD_WAIT(entity=EventEntity)
  1: 0x0010 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res1" with entities [EventEntity, EventEntity]
  2: 0x001D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res1" with entities [EventEntity, EventEntity]
  3: 0x002A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res1" with entities [EventEntity, EventEntity]
  4: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res1" with entities [EventEntity, EventEntity]
  5: 0x0044 [0x00] END_REQSTACK()
```
