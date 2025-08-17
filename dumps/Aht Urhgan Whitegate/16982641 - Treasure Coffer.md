# 16982641 - Treasure Coffer

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 168 bytes                     |
| Total Events     | 5                             |
| References Count | 6                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     59 |             10 |
| [65535.2](#event-655352) | 0x003C       |     36 |              5 |
| [980](#event-980)        | 0x0060       |      6 |              2 |
| [989](#event-989)        | 0x0066       |      6 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0006      |           6 |
|       1 | 0x03C2      |         962 |
|       2 | 0x03C9      |         969 |
|       3 | 0x03C1      |         961 |
|       4 | 0x002B      |          43 |
|       5 | 0x0000      |           0 |

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
| Data Size    | 59 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 03 10 00 80 05 21  00 02 03 10 00 80 01 19   ......!........
0010: 00 03 00 00 01 80 01 1E  00 03 00 00 02 80 01 26  ...............&
0020: 00 03 00 00 03 80 B6 00  00 00 62 04 80 F8 FF FF  ..........b.....
0030: 7F F8 FF FF 7F 6D 61 69  6E 05 80 00              .....main...    
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[3] > 6*) GOTO 0x0021
  1: 0x0009 [0x02] IF !(Work_Zone[3] == 6*) GOTO 0x0019
  2: 0x0011 [0x03] ExtData[1]->WorkLocal[0] = 962*
  3: 0x0016 [0x01] GOTO 0x001E
  4: 0x0019 [0x03] ExtData[1]->WorkLocal[0] = 969*

SUBROUTINE_001E:
  5: 0x001E [0x01] GOTO 0x0026
  6: 0x0021 [0x03] ExtData[1]->WorkLocal[0] = 961*

SUBROUTINE_0026:
  7: 0x0026 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=ExtData[1]->WorkLocal[0])
  8: 0x002A [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[43*, 0*]
  9: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 36 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      7A 05 71 22              z.q"
0040: 03 01 02 00 00 01 80 01  5F 00 B6 00 01 80 62 04  ........_.....b.
0050: 80 F8 FF FF 7F F8 FF FF  7F 6D 61 69 6E 05 80 00  .........main...
```

#### Opcodes

```
  0: 0x003C [0x7A] VM_CONTROL: Reset copy state for Treasure Coffer (ID: 16982641/0x01032271)
  1: 0x0042 [0x02] IF !(ExtData[1]->WorkLocal[0] == 962*) GOTO 0x005F
  2: 0x004A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=962*)
  3: 0x004E [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[43*, 0*]
  4: 0x005F [0x00] END_REQSTACK()
```

### Event 980

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 03 00 00 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0060 [0x03] ExtData[1]->WorkLocal[0] = 962*
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 989

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   03 00  00 01 80 00                    ......    
```

#### Opcodes

```
  0: 0x0066 [0x03] ExtData[1]->WorkLocal[0] = 962*
  1: 0x006B [0x00] END_REQSTACK()
```
