# 17248935 - Honoi-Gomoi

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 68 bytes                    |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [920](#event-920)        | 0x0001       |      9 |              3 |
| [65535.1](#event-655351) | 0x000A       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x3B905     |      243973 |
|       2 | 0x3EC6      |       16070 |
|       3 | 0xFFFFE70F  |  4294960911 |

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

### Event 920

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F A5  01 00                     .........      
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0xA5] EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam
  2: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                32 00 80 1F 00 01            2.....
0010: 80 02 80 03 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x000A [0x32] ExtData[1]->MainSpeed = 1* * 0.1
  1: 0x000D [0x1F] MOVE_ENTITY: EventEntity moves to X=243.973*, Z=16.070*, Y=-6.385*
  2: 0x0015 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0017 [0x00] END_REQSTACK()
```
