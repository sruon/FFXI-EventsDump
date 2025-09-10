# 16998927 - Ashutarihu

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Arrapago Reef (ID: 54) |
| Block Size       | 60 bytes               |
| Total Events     | 2                      |
| References Count | 3                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3](#event-3)         | 0x0001       |     21 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F4D      |        8013 |
|       1 | 0x1F4F      |        8015 |
|       2 | 0x0001      |           1 |

## String References

- **8013**: $!7. $3A$3V$3$5$3^$3$3t$6p$P10h%L7iL$3J$3iIH
- **8015**: $P10h%L$s [5$3\`$3F$3b$3N$6B /

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

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 03 01 10 02 80 A7 00   ...#...#.......
0010: A7 01 01 10 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=8013*)
    → "$!7. $3A$3V$3$5$3^$3$3t$6p$P10h%L7iL$3J$3iIH"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=8015*)
    → "$P10h%L$s [5$3`$3F$3b$3N$6B /"
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x03] Work_Zone[1] = 1*
  5: 0x000E [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response (Dynamis/MMM/Salvage), mode=0x00
  6: 0x0010 [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response with parameter (Dynamis/MMM/Salvage), param=Work_Zone[1]
  7: 0x0014 [0x21] END_EVENT
  8: 0x0015 [0x00] END_REQSTACK()
```
