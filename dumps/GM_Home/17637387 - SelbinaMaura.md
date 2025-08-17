# 17637387 - SelbinaMaura

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 184 bytes         |
| Total Events     | 2                 |
| References Count | 13                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [23](#event-23)       | 0x0001       |    106 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BAC      |        7084 |
|       1 | 0x0000      |           0 |
|       2 | 0x0064      |         100 |
|       3 | 0x0001      |           1 |
|       4 | 0x0065      |         101 |
|       5 | 0x0002      |           2 |
|       6 | 0x0066      |         102 |
|       7 | 0x0003      |           3 |
|       8 | 0x0067      |         103 |
|       9 | 0x0004      |           4 |
|      10 | 0x0068      |         104 |
|      11 | 0x0005      |           5 |
|      12 | 0x0069      |         105 |

## String References

- **7084**: BAAAAAAA (what do you want)? [Time passed for the cooking quest./1 week passed for the clay quest./Down to the last monument./9999 moat carps (San d'Oria)./LV 100 Chocobo!/Check Chocobo level.]

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

### Event 23

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 106 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 19   $......%.......
0010: 00 03 01 10 02 80 01 69  00 02 00 10 03 80 00 29  .......i.......)
0020: 00 03 01 10 04 80 01 69  00 02 00 10 05 80 00 39  .......i.......9
0030: 00 03 01 10 06 80 01 69  00 02 00 10 07 80 00 49  .......i.......I
0040: 00 03 01 10 08 80 01 69  00 02 00 10 09 80 00 59  .......i.......Y
0050: 00 03 01 10 0A 80 01 69  00 02 00 10 0B 80 00 69  .......i.......i
0060: 00 03 01 10 0C 80 01 69  00 21 00                 .......i.!.     
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7084*, default_option=0*, option_flags=0*)
    → "BAAAAAAA (what do you want)? [Time passed for the cooking quest./1 week passed for the clay quest./Down to the last monument./9999 moat carps (San d'Oria)./LV 100 Chocobo!/Check Chocobo level.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 100*
  4: 0x0016 [0x01] GOTO 0x0069
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0029
  6: 0x0021 [0x03] Work_Zone[1] = 101*
  7: 0x0026 [0x01] GOTO 0x0069
  8: 0x0029 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0039
  9: 0x0031 [0x03] Work_Zone[1] = 102*
 10: 0x0036 [0x01] GOTO 0x0069
 11: 0x0039 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0049
 12: 0x0041 [0x03] Work_Zone[1] = 103*
 13: 0x0046 [0x01] GOTO 0x0069
 14: 0x0049 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0059
 15: 0x0051 [0x03] Work_Zone[1] = 104*
 16: 0x0056 [0x01] GOTO 0x0069
 17: 0x0059 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0069
 18: 0x0061 [0x03] Work_Zone[1] = 105*
 19: 0x0066 [0x01] GOTO 0x0069

SUBROUTINE_0069:
 20: 0x0069 [0x21] END_EVENT
 21: 0x006A [0x00] END_REQSTACK()
```
