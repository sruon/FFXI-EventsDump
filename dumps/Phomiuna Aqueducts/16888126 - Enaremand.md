# 16888126 - Enaremand

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Phomiuna Aqueducts (ID: 27) |
| Block Size       | 100 bytes                   |
| Total Events     | 3                           |
| References Count | 8                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [38](#event-38)          | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFCA74E  |  4294747982 |
|       1 | 0x456E      |       17774 |
|       2 | 0xFFFFE890  |  4294961296 |
|       3 | 0x0981      |        2433 |
|       4 | 0x000D      |          13 |
|       5 | 0x003C      |          60 |
|       6 | 0xFFFC9C43  |  4294745155 |
|       7 | 0x4844      |       18500 |

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

### Event 38

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 2F 00 3E B1 01 01   7......../.>...
0010: 4E 00 3E B1 01 01 00                              N.>....         
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-219.314*, z=17.774*, y=-6.000*, direction=213.8°*
  1: 0x000A [0x2F] Enaremand (ID: 16888126/0x0101B13E)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0010 [0x4E] SET_ENTITY_HIDE_FLAG: Show Enaremand (ID: 16888126/0x0101B13E)
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  04 80 1C 05 80 1F 00 06         2........
0020: 80 07 80 02 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001A [0x1C] WAIT(60* ticks)
  2: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-222.141*, Z=18.500*, Y=-6.000*
  3: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0027 [0x00] END_REQSTACK()
```
